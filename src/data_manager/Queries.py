from Server.dbconnect.mysql_repository import repo
from Server.dbconnect.daos import *
from Server.dbconnect.movies import imdb_conn
from Server.dbconnect.books import google_books_conn as book_conn
import datetime, uuid, sys

max_int = 2147483647

def search_by_type(item_type, keywords):
    data_list = []
    if item_type == "movie":
        movies_list = imdb_conn.search(keywords)
        _order_movie_list(movies_list, data_list)
    elif item_type == "book":
        books_list = book_conn.search(keywords)
        _order_books_list(books_list, data_list)
    return {'data': data_list}


def get_item_info(item_id):
    media_list = repo.media.find_by(id=item_id)
    if media_list:
        media = media_list[0]
        if media.media_type == "movie":
            movie_list = imdb_conn.search(media.name)
            if movie_list:
                movie = movie_list[0]
                movie_data = vars(movie)
                _update_movie_db(movie)
                _add_data_to_media(movie, movie_data)
                return movie_data
        elif media.media_type == "book":
            books = book_conn.search(media.name)
            book_id = _get_book_id(media)
            # search for the right book
            book = _find_book_by_id(book_id, books)
            if book:
                book_data = vars(book)
                _update_book_db(book)
                _add_data_to_media(book, book_data)
                return book_data
    return {}


def search_favorites(category):
    media_list = repo.media.limited_find_by(type=category)
    all_results = _order_media_list_top(media_list, category)
    return {'data': all_results}


def add_review(item_id, rating, bravery_moments, content, reviewer):
    repo.reviews.insert(Review(item_id, content, reviewer, rating, datetime.datetime.now()))
    repo.braveryMoment.insert(BraveryMoment(item_id, bravery_moments))


# region private methods


def _order_movie_list(movies_list, data_list):
    for movie in movies_list:
        media_data = vars(movie)
        _update_movie_db(movie)
        _add_data_to_media(movie, media_data)
        data_list.append(media_data)
    return data_list


def _order_books_list(books_list, data_list):
    for book in books_list:
        _generate_book_id(book)
        book_data = vars(book)
        _update_book_db(book)
        _add_data_to_media(book, book_data)
        data_list.append(book_data)
    return data_list


def _update_movie_db(movie):
    media = repo.media.find_by(id=movie.id)
    if not media:
        repo.media.insert(Media(movie.title, "movie", movie.id))


def _update_book_db(book):
    media = repo.media.find_by(id=book.id)
    if not media:
        repo.media.insert(Media(book.title, "book", book.id))


def _add_data_to_media(media, data):
    _add_bravery_rate(media.id, data)
    _add_heroism_moments(media.id, data)
    _add_recommendations(media.id, data)


def _add_bravery_rate(media_id, data):
    rate = repo.reviews.get_average_rating(media_id)
    if not rate:
        rate = "null"
    data['braveryRate'] = rate


def _add_heroism_moments(movie_id, data):
    moments_obj_list = repo.braveryMoment.find_by(media_id=movie_id)
    moments = []
    for moment in moments_obj_list:
        moments.append(moment.start)
    data['selectedHeroismMoments'] = moments


def _add_recommendations(movie_id, data):
    reviews_obj_list = repo.reviews.find_by(media_id=movie_id)
    reviews = []
    for recommendation in reviews_obj_list:
        reviews.append(recommendation.review)
    data['recommendations'] = reviews


def _order_media_list_top(media_list, category):
    data_list = []
    if category == "movie":
        for movie in media_list:
            data_list.append(get_item_info(movie.id))
    elif category == "book":
        for book in media_list:
            data_list.append(get_item_info(book.id))
    return data_list


def _generate_book_id(book):
    book_id = book.id
    book_uuid = uuid.uuid1().int % max_int
    repo.uuidMap.insert(UuidMap(book_uuid, book_id))
    book.id = book_uuid


def _get_book_id(book):
    uuid_map = repo.uuidMap.find_by(uuid=book.id)
    if not uuid_map:
        raise Exception("book with id: {} not found in bravery-media db.".format(book.id))
    return uuid_map[0].string_id


def _find_book_by_id(book_id, books):
    for book in books:
        if book.id == book_id:
            return book
    return None
# endregion
