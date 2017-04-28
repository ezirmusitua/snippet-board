from time import time
import hashlib
from flask import render_template, request
from ..database import SqliteDB
from . import snippet


@snippet.route('/', methods=['GET'])
def list_snippet():
    snippets = SqliteDB.select(None, 'snippet')
    return render_template('index.html', snippets=snippets)


@snippet.route('/api/v0.1.0', methods=['POST'])
def route_to_post_snippet():
    fields = ('link_hash', 'raw_content', 'create_at', 'create_by')
    snippet = request.get_json()
    snippet['raw_content'] = '\'' + \
        snippet['raw_content'].replace('\'', '\\\'') + '\''
    snippet['create_by'] = 'jferroal'
    snippet['create_at'] = time() * 1000
    snippet['link_hash'] = hashlib.sha1(snippet['link']).hexdigest()
    snippet_values = [snippet[key] for key in fields]
    SqliteDB.insert('snippet', fields, snippet_values)
    return 'create snippet successed'
