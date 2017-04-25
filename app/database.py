"""use sqlalchemy in Future version"""
import sqlite3
from types import *


def concat_query_value_with_type(prev, _value):
    if type(_value) is StringType:
        return prev + '\'' + _value + '\', '
    else:
        return prev + str(_value) + ', '


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
        print SqliteDB.dbpath
        if SqliteDB.db is None:
            SqliteDB.db = sqlite3.connect(SqliteDB.dbpath)

    @staticmethod
    def _disconnect():
        if SqliteDB.db is not None:
            SqliteDB.db.close()
            SqliteDB.db = None

    @staticmethod
    def _fetch_all_as_array(cursor):
        result = list()
        for row in cursor.fetchall():
            for idx, value in enumerate(row):
                print row
                result.append({cursor.description[idx][0]: value})
        return result
        # return [dict((cursor.description[idx][0], value)
        # for idx, value in enumerate(row) for row in cursor.fetchall())]

    @staticmethod
    def _select_without_where(_fields, _from):
        SqliteDB._connect()
        field_str = '(' + ', '.join(_fields) + \
            ')' if _fields is not None else '*'
        query_str = 'SELECT ' + field_str + ' FROM ' + _from + ';'
        cursor = SqliteDB.db.execute(query_str)
        result = SqliteDB._fetch_all_as_array(cursor)
        SqliteDB._disconnect()
        return result

    @staticmethod
    def _select_with_where(_fields, _from, where=None):
        SqliteDB._connect()
        field_str = '(' + ', '.join(_fields) + \
            ')' if _fields is not None else '*'
        where_str = reduce(lambda prev, dict_item: prev +
                           dict_item[0] + '=' + dict_item[1], where.items(), '')
        query_str = 'SELECT ' + field_str + ' FROM ' + \
            _from + ' WHERE ' + where_str + ';'
        cursor = SqliteDB.db.execute(query_str)
        result = SqliteDB._fetch_all_as_array(cursor)
        SqliteDB._disconnect()
        return result

    @staticmethod
    def select(_fields, _from, _where=None):
        if _where is None:
            SqliteDB._select_without_where(_fields, _from)
        else:
            SqliteDB._select_with_where(_fields, _from)

    @staticmethod
    def _insert_without_fields(table, _values):
        SqliteDB._connect()
        value_str = '(' + reduce(concat_query_value_with_type,
                                 _values, '')[:-2] + ')'
        query_str = 'INSERT INTO ' + table + ' VALUES ' + value_str + ';'
        print 'Query string: ', query_str
        SqliteDB.db.execute(query_str)
        SqliteDB.db.commit()
        SqliteDB._disconnect()

    @staticmethod
    def _insert_with_fields(table, _fields, _values):
        SqliteDB._connect()
        field_str = '(' + ', '.join(_fields) + ')'
        value_str = '(' + reduce(concat_query_value_with_type,
                                 _values, '') + ')'
        query_str = 'INSERT INTO ' + table + \
            ' VALUES ' + field_str + ' ' + value_str + ';'
        print 'Query string: ', query_str
        SqliteDB.db.execute(query_str)
        SqliteDB.db.commit()
        SqliteDB._disconnect()

    @staticmethod
    def insert(table, _fields_or_values, _values=None):
        if _values is None:
            SqliteDB._insert_without_fields(table, _fields_or_values)
        else:
            SqliteDB._insert_with_fields(table, _fields, _values)
