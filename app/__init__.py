# -*- coding: utf-8 -*-
import os
import sqlite3
from flask import Flask, g, render_template
from database import SqliteDB

DATABASE = os.path.abspath('../db/snippet_board.db')

app = Flask(__name__)
database = SqliteDB(DATABASE)


@app.route('/', methods=['GET'])
def route_to_index():
    # fetch snippets from db
    snippets = SqliteDB.select(None, 'snippet')
    print snippets
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
