import hashlib
from time import time
from . import db


class Snippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link_hash = db.Column(db.String(), unique=True)
    create_at = db.Column(db.String())
    raw_content = db.Column(db.String())
    create_by = db.Column(db.String())

    def __init__(self, snippet_body):
        print(snippet_body)
        self.link_hash = hashlib.sha1(snippet_body['link'].encode()).hexdigest()
        self.raw_content = snippet_body['raw_content']
        self.create_by = snippet_body.get('create_by', 'jferroal')
        self.create_at = time() * 1000

    def __repr__(self):
        return '<Snippet %r>' % self.link_hash


class DownloadTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    download_id = db.Column(db.String(), unique=True)
    create_at = db.Column(db.String())
    create_by = db.Column(db.String())
    download_uri = db.Column(db.String())

    def __init__(self, taskBody):
        self.title = taskBody.get('title')
        self.create_at = time() * 1000
        self.create_by = taskBody.get('createBy', 'jferroal')
        self.download_id = taskBody.get('download_id')
        self.download_uri = taskBody.get('download_uri')

    def __repr__(self):
        return '<DownloadTask %r>' % self.title
