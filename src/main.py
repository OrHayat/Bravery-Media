from data_manager import Queries
from Server.dbconnect.mysql_repository import repo

if __name__ == '__main__':
    # run only once!!!!!!
    repo.drop_tables()
    #-------------------

    repo.create_tables()

    # add data to db
    book1 = Queries.search_by_type("book", "shindler")
    book2 = Queries.search_by_type("book", "diary")

    movie1 = Queries.search_by_type("movie", "pyjama")
    movie2 = Queries.search_by_type("movie", "pianist")

    # check and add more ids if you want to
    id1 = book1['data'][0]['id']
    id2 = book2['data'][0]['id']
    id3 = movie1['data'][0]['id']

    #  add reviews for tests
    Queries.add_review(id1, 8, 34, "aaa", 0)
    Queries.add_review(id1, 1, 354, "bbb", 0)
    Queries.add_review(id2, 10, 44, "ccc", 0)
    Queries.add_review(id2, 4, 3464, "ddd eee fff", 0)

    # check that the media is in the db
    x1 = Queries.get_item_info(id1)
    x2 = Queries.get_item_info(id2)
