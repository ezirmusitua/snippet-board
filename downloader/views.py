from flask import render_template, request
import requests
from . import downloader


@downloader.route('/api/v0.1.0', methods=['POST'])
def start_download_task():
    return 'hello downloader'
