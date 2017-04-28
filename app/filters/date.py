import datetime


def formatDate(timestamp, fmt=None):
    _format = '%Y/%m/%d'
    if fmt is not None:
        _format = fmt
    return datetime.datetime.fromtimestamp(int(timestamp / 1000)).strftime(_format)
