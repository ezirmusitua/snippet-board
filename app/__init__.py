# -*- coding: utf-8 -*-
import sqlite3
from flask import Flask, g
from database import SqliteDB

DATABASE = '../db/snippet_board.db'

app = Flask(__name__)
database = SqliteDB(DATABASE)


@app.route('/')
def hello_world():
    SqliteDB.insert('snippet', ('0dbeaf4d8c0d88aa095b5deee78998fc21081b9d',
                                '1492616636890', 'Date: 2017-4-19[23:44]\nContent:\n组织你的项目', 'jferroal'))
    return 'hello world'


if __name__ == '__main__':
    app.run()
