from flask import Blueprint

downloader = Blueprint('downloader', __name__)

from . import views
