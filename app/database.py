import sqlite3


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SqliteDB(object):
    __metaclass__ = Singleton
    dbpath = None
    db = None

    def __init__(self, dbpath='./default.db'):
        SqliteDB.dbpath = dbpath

    @staticmethod
    def _connect():
        if SqliteDB.db is None:
            SqliteDB.db = sqlite3.connect(SqliteDB.dbpath)

    @staticmethod
    def _disconnect():
        if SqliteDB.db is not None:
            SqliteDB.db.close()
            SqliteDB.db = None

    @staticmethod
    def _fetch_all_as_array(cursor):
        return [dict((cursor.description[idx][0], value)
                     for idx, value in enumerate(row) for row in cur.fetchall())]

    @staticmethod
    def select(_fields, _from):
        SqliteDB._connect()
        field_str = '(' + ', '.join(_fields) + \
            ')' if field is not None else '*'
        cursor = SqliteDB.db.execute('SELECT ? FROM ?;', [field_str, _from])
        result = SqliteDB._fetch_all_as_array(cursor)
        SqliteDB._disconnect()
        return result

    @staticmethod
    def select(_fields, _from, where):
        SqliteDB._connect()
        field_str = '(' + ', '.join(_fields) + \
            ')' if field is not None else '*'
        where_str = reduce(lambda prev, dict_item: prev +
                           dict_item[0] + '=' + dict_item[1], where.items(), '')
        cursor = SqliteDB.db.execute('SELECT ? FROM ? WHERE ?;', [
            field_str, _from, where_str])
        result = SqliteDB._fetch_all_as_array(cursor)
        SqliteDB._disconnect()
        return result

    @staticmethod
    def _insert_without_fields(table, _values):
        SqliteDB._connect()
        value_str = '(' + ', '.join(_values) + ')'
        SqliteDB.db.execute('INSERT into ' + table +
                            ' VALUES ' + value_str + ';')
        SqliteDB._disconnect()

    @staticmethod
    def _insert_with_fields(table, _fields, _values):
        SqliteDB._connect()
        field_str = '(' + ', '.join(_fields) + ')'
        value_str = '(' + ', '.join(_values) + ')'
        SqliteDB.db.execute('INSERT into ' + field_str +
                            ' ' + table + ' VALUES ' + value_str + ';')
        SqliteDB._disconnect()

    @staticmethod
    def insert(table, _fields_or_values, _values=None):
        if _values is None:
            SqliteDB._insert_without_fields(table, _fields_or_values)
        else:
            SqliteDB._insert_with_fields(table, _fields, _values)
