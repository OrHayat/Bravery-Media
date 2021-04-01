import atexit
import MySQLdb
from Server.dbconnect.daos import _UuidMap, _Users, _Reviews, _Medias, _BraveryMoments
import Server.dbconnect.dbconfig as config


class _Repository:
    def __init__(self):
        # replace with AWS db location
        self._conn = MySQLdb.connect( host= config.remote_db_hostname,
                                      user= config.remote_db_username,
                                      passwd= config.remote_db_password,
                                      db= config.remote_db_database)
        self.cursor = self._conn.cursor()
        self.users = _Users(self.cursor)
        self.reviews = _Reviews(self.cursor)
        self.media = _Medias(self.cursor)
        self.braveryMoment = _BraveryMoments(self.cursor)
        self.uuidMap = _UuidMap(self.cursor)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    """
    TEMP FOR NOW
    """

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bm_users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        type TEXT NOT NULL
        );""")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bm_idMap(
        uuid INTEGER PRIMARY KEY,
        string_id TEXT NOT NULL
        );""")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bm_medias(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT NOT NULL
        );""")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bm_reviews(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        media_id INTEGER NOT NULL,
        review TEXT NOT NULL,
        reviewer INTEGER NOT NULL,
        date DATE NOT NULL,
        rating INTEGER NOT NULL,
        FOREIGN KEY(media_id) REFERENCES bm_medias(id)
        
        );""")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bm_braveryMoments(
        id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        media_id INTEGER NOT NULL,
        start INTEGER NOT NULL,
        FOREIGN KEY(media_id) REFERENCES bm_medias(id) ON DELETE CASCADE
        );
        """)
    #  ON DELETE CASCADE
    def drop_tables(self):
        for table_name in config.table_names:
            self.cursor.execute("""
                    DROP TABLE IF EXISTS {}
                    """.format(table_name))


repo = _Repository()
atexit.register(repo._close)
