from Server.dbconnect.dtos import Review, User, Media, BraveryMoment, UuidMap
from Server.dbconnect.dbconfig import dbvalues


# TODO remove if not used later
def _limit_media_results(lst):
    if len(lst) > dbvalues["media_limit"]:
        return lst[:50]


class _Reviews:
    def __init__(self, curr):
        self._curr = curr

    def insert(self, review):
        self._curr.execute("""
        INSERT INTO bm_reviews (media_id, date, rating, review, reviewer) VALUES (%s, %s, %s, %s, %s)

        """, review.get_sorted_vars()[1:])

    def find_by(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()

        stmt = 'SELECT * FROM bm_reviews WHERE {}'.format(' AND '.join([col + '=%s' for col in column_names]))

        c = self._curr
        c.execute(stmt, list(params))
        return [Review(*row[1:], row[0]) for row in c.fetchall()]

    def delete(self, id):
        self._curr.execute("""
                DELETE FROM bm_reviews WHERE id=%s
                """, (str(id)))

    def update(self, id, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
        stmt = 'Update bm_reviews SET {} WHERE id={}'.format(' AND '.join([col + '=%s' for col in column_names]), id)
        self._conn.execute(stmt, list(params))

    def get_reviews_by_date(self):
        c = self._curr
        c.execute("""
        SELECT * FROM bm_reviews ORDER BY date ASC
        """)
        return [Review(*row[1:], row[0]) for row in c.fetchall()]

    def sum_column(self, col_name):
        c = self._curr
        c.execute("""
        SELECT SUM({}) FROM bm_reviews
        """.format(col_name))
        return c.fetchone()[0]

    def get_average_rating(self, media_id):
        c = self._curr
        c.execute("""
               SELECT avg(rating) FROM bm_reviews Where media_id ={}
               """.format(media_id))
        return c.fetchone()[0]


class _Users:
    def __init__(self, curr):
        self._curr = curr

    def insert(self, user):
        self._curr.execute("""
        INSERT INTO bm_users (name, type) VALUES (%s, %s)
        """, user.get_sorted_vars()[1:])

    def find_by(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()

        stmt = 'SELECT * FROM bm_users WHERE {}'.format(' AND '.join([col + '=%s' for col in column_names]))

        c = self._curr
        c.execute(stmt, list(params))
        return [User(*row[1:], row[0]) for row in c.fetchall()]

    def limited_find_by(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()

        stmt = 'SELECT * FROM bm_users WHERE {} LIMIT {}'.format(' AND '.join([col + '=%s' for col in column_names]),
                                                             dbvalues["media_limit"])

        c = self._curr
        c.execute(stmt, list(params))
        return [User(*row[:]) for row in c.fetchall()]

    def delete(self, id):
        self._curr.execute("""
                DELETE FROM bm_users WHERE id=%s
                """, (str(id)))

    def update(self, id, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
        stmt = 'Update bm_users SET {} WHERE id={}'.format(' AND '.join([col + '=%s' for col in column_names]), id)
        self._curr.execute(stmt, list(params))


class _Medias:
    def __init__(self, curr):
        self._curr = curr

    def insert(self, media):
        self._curr.execute("""
        INSERT INTO bm_medias (id, name , type) VALUES (%s, %s, %s)
        """, media.get_sorted_vars())

    def find_by(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()

        stmt = "SELECT * FROM bm_medias WHERE {}".format(' AND '.join([col + '=%s' for col in column_names]))

        c = self._curr
        c.execute(stmt, list(params))
        return [Media(*row[1:], row[0]) for row in c.fetchall()]

    def delete(self, id):
        self._curr.execute("""
                DELETE FROM bm_medias WHERE id=%s
                """, (str(id)))

    def update(self, id, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
        stmt = 'Update bm_medias SET {} WHERE id={}'.format(' AND '.join([col + '=%s' for col in column_names]), id)
        self._curr.execute(stmt, list(params))

    def sum_column(self, col_name):
        c = self._curr
        c.execute("""
        SELECT SUM({}) FROM bm.medias
        """.format(col_name))
        return c.fetchone()[0]

    def limited_find_by(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()

        stmt = 'SELECT * FROM bm_medias WHERE {} LIMIT {}'.format(' AND '.join([col + '=%s' for col in column_names]),
                                                             dbvalues["media_limit"])

        c = self._curr
        c.execute(stmt, list(params))
        return [Media(*row[1:], row[0]) for row in c.fetchall()]


class _BraveryMoments:
    def __init__(self, curr ):
        self._curr = curr

    def insert(self, bravery_moment):
        self._curr.execute("""
        INSERT INTO bm_braveryMoments (media_id , start) VALUES (%s, %s)
        """, bravery_moment.get_sorted_vars()[1:])

    def find_by(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()

        stmt = 'SELECT * FROM bm_braveryMoments WHERE {}'.format(' AND '.join([col + '=%s' for col in column_names]))

        c = self._curr
        c.execute(stmt, list(params))
        return [BraveryMoment(*row[1:], row[0]) for row in c.fetchall()]

    def delete(self, id):
        self._curr.execute("""
                DELETE FROM bm_braveryMoments WHERE id=%s
                """, (str(id)))

    def update(self, id, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
        stmt = 'Update bm_braveryMoments SET {} WHERE id={}'.format(' AND '.join([col + '=%s' for col in column_names]), id)
        self._curr.execute(stmt, list(params))

    def sum_column(self, col_name):
        c = self._curr
        c.execute("""
        SELECT SUM({}) FROM bm_braveryMoments
        """.format(col_name))
        return c.fetchone()[0]


class _UuidMap:
    def __init__(self, curr):
        self._curr = curr

    def insert(self, uuidmap):
        self._curr.execute("""
        INSERT INTO bm_idMap (uuid, string_id) VALUES (%s, %s)

        """, uuidmap.get_sorted_vars()[:])

    def find_by(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()

        stmt = 'SELECT * FROM bm_idMap WHERE {}'.format(' AND '.join([col + '=%s' for col in column_names]))

        c = self._curr
        c.execute(stmt, list(params))
        return [UuidMap(*row[:]) for row in c.fetchall()]


