from data_manager import Queries
from Server.dbconnect.mysql_repository import repo
from Server.dbconnect.books import google_books_conn as conn

if __name__ == '__main__':
    repo.create_tables()
    # movies1 = Queries.search_by_type("movie", "pianist")
    # movies2 = Queries.search_by_type("movie", "pijama")
    # book = conn.search("shindler")
    # book1 = Queries.search_by_type("book", "shindler")
    # book2 = Queries.search_by_type("book", "diary")

    import hashids
    
    x=0
    Queries._convert_str_id_to_int('rnDWBQAAQBAJ')
    # id1 = 423
    # id2 = 14574
    #
    # Queries.add_review(id1, 8, 34, "aaa", 0)
    # Queries.add_review(id1, 1, 354, "bbb", 0)
    # Queries.add_review(id2, 10, 44, "ccc", 0)
    # Queries.add_review(id2, 4, 3464, "ddd eee fff", 0)
    #
    # x1 = Queries.get_item_info(id1)
    # x2 = Queries.get_item_info(id2)

    # id1 = list(book1.keys())[0]
    # id2 = list(book2.keys())[0]


    Queries._convert_str_id_to_int(id1)

    # Queries.add_review(id1, 8, 34, "aaa", 0)
    # Queries.add_review(id1, 1, 354, "bbb", 0)
    # Queries.add_review(id2, 10, 44, "ccc", 0)
    # Queries.add_review(id2, 4, 3464, "ddd eee fff", 0)

    x1 = Queries.get_item_info(id1)
    x2 = Queries.get_item_info(id2)
    t=0
