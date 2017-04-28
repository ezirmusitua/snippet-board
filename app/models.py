import hashlib
from time import time
from flask_sqlalchemy import SQLAlchemy
from . import db


class Snippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link_hash = db.Column(db.String(), unique=True)
    create_at = db.Column(db.String(), unique=True)
    raw_content = db.Column(db.String())
    create_by = db.Column(db.String())

    def __init__(self, snippetBody):
        self.link_hash = hashlib.sha1(snippetBody['link']).hexdigest()
        self.raw_content = snippetBody['raw_content']
        self.create_by = snippetBody.get('create_by', 'jferroal')
        self.create_at = time() * 1000

    def __repr__(self):
        return '<Snippet %r>' % self.link_hash
