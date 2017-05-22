from flask import render_template, request
import requests
from . import downloader
from .aira2_req import Aria2Req
from ..models import DownloadTask
from .. import db


@downloader.route('/api/v0.1.0/task', methods=['POST'])
def start_download_task():
    task_body = request.get_json()
    existed_tasks = DownloadTask.query.filter_by(title=task_body['name']).all()
    if len(existed_tasks) > 0:
        return 'task existed'
    add_uri_req = Aria2Req().addUri(
        task_body['name'], [task_body['uri']])
    res_json = requests.post(
        'http://localhost:6800/jsonrpc', add_uri_req).json()
    task = DownloadTask({
        'title': res_json['id'],
        'download_id': res_json['result'],
        'download_uri': task_body['uri'],
    })
    db.session.add(task)
    db.session.commit()
    return 'starting download %s, gid: %s' % (res_json['id'], res_json['result'])


@downloader.route('/api/v0.1.0/task/<gid>', methods=['GET'])
def tell_status(gid):
    tell_status_req = Aria2Req().tellStatus(gid)
    res = requests.post('http://localhost:6800/jsonrpc', tell_status_req)
    return res.content


@downloader.route('/api/v0.1.0/task', methods=['GET'])
def tell_all_status():
    tasks = DownloadTask.query.all()
    tasks_status = list()
    for task in tasks:
        tell_status_req = Aria2Req().tellStatus(task.download_id)
        tasks_status.append(requests.post(
            'http://localhost:6800/jsonrpc', tell_status_req).json())
    print tasks_status
    return '111'
