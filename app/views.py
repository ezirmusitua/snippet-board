from flask import render_template
from . import app
from database import SqliteDB


def route_to_index():
    return render_template('index.html')
