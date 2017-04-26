# -*- coding: utf-8 -*-
import os
import sqlite3
import hashlib
import datetime
from time import time
from flask import Flask, g, render_template, request
from database import SqliteDB

DATABASE = os.path.abspath('../db/snippet_board.db')

app = Flask(__name__)
database = SqliteDB(DATABASE)


@app.route('/', methods=['GET'])
@app.route('/snippet', methods=['GET'])
def route_to_index():
    # fetch snippets from db
    snippets = SqliteDB.select(None, 'snippet')
    return render_template('index.html', snippets=snippets)


@app.route('/snippet/api/v0.1.0', methods=['POST'])
def route_to_post_snippet():
    fields = ('link_hash', 'raw_content', 'create_at', 'create_by')
    snippet = request.get_json()
    snippet['raw_content'] = str(snippet['raw_content'])
    snippet['create_by'] = 'jferroal'
    snippet['create_at'] = time() * 1000
    snippet['link_hash'] = hashlib.sha1(snippet['link']).hexdigest()
    for key in fields:
        print key, snippet[key]
    snippet_values = [snippet[key] for key in fields]
    print snippet_values
    SqliteDB.insert('snippet', fields, snippet_values)
    return 'hello world'


@app.template_filter('date')
def _jinja2_filter_datetime(timestamp, fmt=None):
    _format = '%Y/%m/%d'
    if fmt is not None:
        _format = fmt
    return datetime.datetime.fromtimestamp(int(timestamp / 1000)).strftime(_format)


if __name__ == '__main__':
    app.run(debug=True)
