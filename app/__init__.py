# -*- coding: utf-8 -*-
import os
import sqlite3
import datetime
from flask import Flask, g, render_template
from database import SqliteDB

DATABASE = os.path.abspath('../db/snippet_board.db')

app = Flask(__name__)
database = SqliteDB(DATABASE)


@app.route('/', methods=['GET'])
def route_to_index():
    # fetch snippets from db
    snippets = SqliteDB.select(None, 'snippet')
    return render_template('index.html', snippets=snippets)


@app.template_filter('date')
def _jinja2_filter_datetime(timestamp, fmt=None):
    _format = '%Y/%m/%d'
    if fmt is not None:
        _format = fmt
    return datetime.datetime.fromtimestamp(int(timestamp / 1000)).strftime(_format)


if __name__ == '__main__':
    app.run(debug=True)
