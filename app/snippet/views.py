from time import time
from flask import render_template, request
from ..models import Snippet
from . import snippet
from .. import db


@snippet.route('/', methods=['GET'])
def list_snippet():
    snippets = Snippet.query.all()
    return render_template('index.html', snippets=snippets)


@snippet.route('/api/v0.1.0', methods=['POST'])
def route_to_post_snippet():
    fields = ('link_hash', 'raw_content', 'create_at', 'create_by')
    snippetBody = request.get_json()
    snippet = Snippet(snippetBody)
    db.session.add(snippet)
    db.session.commit()
    return 'create snippet successed'
