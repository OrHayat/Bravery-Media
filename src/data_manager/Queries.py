from Server.dbconnect.mysql_repository import repo
from Server.dbconnect.daos import *
from Server.dbconnect.movies import imdb_conn
from Server.dbconnect.books import google_books_conn as book_conn
import datetime, uuid


def search_by_type(item_type, keywords):
    data = {}
    if item_type == "movie":
        movies_list = imdb_conn.search(keywords)
        _order_media_list(movies_list, data)
    elif item_type == "book":
        books_list = book_conn.search(keywords)
        _order_books_list(books_list, data)
    return data


def get_item_info(item_id):
    data = {}
    media_list = repo.media.find_by(id=item_id)
    if not media_list:
        return data
    media = media_list[0]
    if media.media_type == "movie":
        movie_list = imdb_conn.search(media.name)
        for movie in movie_list:
            data[movie.id] = vars(movie)
            _update_movie_db(movie)
            _add_data_to_media(movie, data[movie.id])
    elif media.media_type == "book":
        books = book_conn.search(media.name)
        for book in books:
            data[media.id] = vars(book)
            _update_book_db(book)
            _add_data_to_media(book, data[book.id])
    return data


def search_favorites(category):
    media_list = repo.media.limited_find_by(type=category)
    return _order_media_list(media_list, {})


def add_review(item_id, rating, bravery_moments, content, reviewer):
    repo.reviews.insert(Review(item_id, content, reviewer, rating, datetime.datetime.now()))
    repo.braveryMoment.insert(BraveryMoment(item_id, bravery_moments))


# region private methods


def _order_media_list(movies_list, data):
    for movie in movies_list:
        data[movie.id] = vars(movie)
        _update_movie_db(movie)
        _add_bravery_rate(movie.id, data[movie.id])
    return data


def _order_books_list(books_list, data):
    for book in books_list:
        # book.id = uuid.uuid1().int % 5000
        data[book.id] = vars(book)
        _update_book_db(book)
        _add_bravery_rate(book.id, data[book.id])


def _update_movie_db(movie):
    media = repo.media.find_by(id=movie.id)
    if not media:
        repo.media.insert(Media(movie.title, "movie", movie.id))


def _update_book_db(book):
    media = repo.media.find_by(id=book.id)
    if not media:
        repo.media.insert(Media(book.title, "book", book.id))


def _add_data_to_media(movie, data):
    _add_bravery_rate(movie.id, data)
    _add_heroism_moments(movie.id, data)
    _add_recommendations(movie.id, data)


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


def _convert_str_id_to_int(str_id):
    str_num = ""
    for c in str_id:
        str_num += str(ord(c))
    return int(str_num)

def _convert_int_id_to_str():
    None

# endregion

