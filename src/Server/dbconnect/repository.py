# import atexit
# import sqlite3
# from Server.dbconnect.daos import _Users, _Reviews, _Medias, _BraveryMoments
# import Server.dbconnect.dbconfig as config
#
#
#
# class _Repository:
#     def __init__(self):
#         # replace with AWS db location
#         self._conn = sqlite3.connect('database.db')
#         self.users = _Users(self._conn)
#         self.reviews = _Reviews(self._conn)
#         self.media = _Medias(self._conn)
#         self.braveryMoment = _BraveryMoments(self._conn)
#
#     def _close(self):
#         self._conn.commit()
#         self._conn.close()
#
#     """
#     TEMP FOR NOW
#     """
#
#     def create_tables(self):
#         self._conn.executescript("""
#         CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY,
#         username TEXT NOT NULL,
#         type TEXT NOT NULL
#         );
#
#         CREATE TABLE IF NOT EXISTS reviews(
#         id INTEGER PRIMARY KEY,
#         media_id NOT NULL,
#         review TEXT NOT NULL,
#         reviewer INTEGER NOT NULL,
#         rating INTEGER NOT NULL,
#         date DATE NOT NULL,
#         FOREIGN KEY(reviewer) REFERENCES users(id)
#         FOREIGN KEY(media_id) REFERENCES media(id)
#         );
#
#         CREATE TABLE IF NOT EXISTS medias(
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         type TEXT NOT NULL
#         );
#
#         CREATE TABLE IF NOT EXISTS braveryMoments(
#         id INTEGER PRIMARY KEY,
#         media_id INTEGER NOT NULL,
#         start INTEGER NOT NULL,
#         FOREIGN KEY(media_id) REFERENCES media(id)
#         );
#         """)
#
#     def drop_tables(self):
#         for table_name in config.table_names:
#             self._conn.executescript("""
#                     DROP TABLE IF EXISTS {}
#                     );
#                     """.format(table_name))
#
#
# repo = _Repository()
# atexit.register(repo._close)
