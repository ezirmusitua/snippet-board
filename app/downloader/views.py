import json
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
    prev_task_stat = requests.post(
        'http://localhost:6800/jsonrpc', tell_status_req).json()['result']
    print json.dumps(prev_task_stat)
    if 'followedBy' in prev_task_stat:
        tell_stat_req = Aria2Req().tellStatus(prev_task_stat['followedBy'])
        task_stat = requests.post(
            'http://localhost:6800/jsonrpc', tell_status_req).json()['result']
    else:
        task_stat = prev_task_stat
    return json.dumps({
        'totalLength': task_stat['totalLength'],
        'completedLength': task_stat['completedLength'],
        'status': task_stat['status']
    })


@downloader.route('/api/v0.1.0/task', methods=['GET'])
def tell_all_status():
    taskNames = map(lambda x: x.strip(), request.args.get('names').split(';'))
    existed_tasks = DownloadTask.query.filter(
        DownloadTask.title.in_(taskNames)).all()
    existed_tasks_name_map = dict()
    for index in range(0, len(existed_tasks)):
        task = existed_tasks[index]
        existed_tasks_name_map[task.title] = index
    task_stat_name_map = dict()
    for taskName in taskNames:
        taskIndex = existed_tasks_name_map.get(taskName, None)
        if taskIndex is not None:
            existed_task = existed_tasks[taskIndex]
            tell_stat_req = Aria2Req().tellStatus(
                existed_task.download_id)
            prev_task_stat = requests.post(
                'http://localhost:6800/jsonrpc', tell_stat_req).json()['result']
            if 'followedBy' in prev_task_stat:
                tell_stat_req = Aria2Req().tellStatus(
                    prev_task_stat['followedBy'][0])
                print 'followed by: ', json.dumps(tell_stat_req)
                task_stat = requests.post(
                    'http://localhost:6800/jsonrpc', tell_stat_req).json()['result']
                print task_stat
            else:
                task_stat = prev_task_stat
            print task_stat['status']
            task_stat_name_map[taskName] = {
                'name': taskName,
                'totalLength': task_stat['totalLength'],
                'completedLength': task_stat['completedLength'],
                'status': task_stat['status'],
                'uri': existed_task.download_uri
            }
        else:
            task_stat_name_map[taskName] = {
                'totalLength': '1',
                'completedLength': '0',
                'status': 'unknown',
                'name': taskName
            }
    return json.dumps(task_stat_name_map)
