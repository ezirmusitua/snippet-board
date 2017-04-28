from flask import Blueprint

snippet = Blueprint('snippet', __name__)

from . import views
