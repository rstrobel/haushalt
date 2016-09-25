
import psycopg2
import sys
import json
import logging
import datetime

class MyDB(object):
    _db_connection = None
    _db_cur = None

    def __init__(self):
        self._db_connection = db_module.connect('host', 'user', 'password', 'db')
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        return self._db_cur.execute(query, params)

    def __del__(self):
        self._db_connection.close()
