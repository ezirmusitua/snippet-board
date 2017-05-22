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
    taskNames = map(lambda x: x.strip(), request.args.get('names').split(';'))
    existed_tasks = DownloadTask.query.filter(
        DownloadTask.id.in_(taskNames)).all()
    existed_task_name_map = dict((task['name'], dict(task, index=index)) for (
        index, task) in enumerate(existed_tasks))
    task_stat_name_map = dict()
    for taskName in taskNames:
        task_stat = dict()
        _taskInfo = existed_task_name_map.get(taskName, None)
        if _taskInfo is not None:
            tell_stat_req = Aria2Req().tellStatus(
                existed_tasks[_taskInfo.index].download_id)
            task_stat = requests.post(
                'http://localhost:6800/jsonrpc', tell_status_req).json()
            task_stat = {
                'length': task_status['length'],
                'completedLength': task_status['completedLength'],
                'status': task_status['status']
            }
        else:
            task_stat = {
                'length': '1',
                'completedLength': '0',
                'status': 'error',
            }
        task_stat_name_map[taskName] = task_stat
    return str(task_stat_name_map)
