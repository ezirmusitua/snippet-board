# -*- coding: utf-8 -*-
import sqlite3
from flask import Flask, g, render_template
from database import SqliteDB

DATABASE = '../db/snippet_board.db'

app = Flask(__name__)
database = SqliteDB(DATABASE)


@app.route('/', methods=['GET'])
def route_to_index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
