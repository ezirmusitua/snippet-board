import json


class Aria2Req(object):
    def __init__(self, jsonrpc_version='2.0', secret=None):
        self.req_body = {'jsonrpc': jsonrpc_version}
        if secret is not None:
            self.req_body['secret'] = secret

    def addUri(self, title, uris, options=None, position=None):
        self.req_body['method'] = 'aria2.addUri'
        self.req_body['id'] = title
        self.req_body['params'] = [uris]
        if options is not None:
            self.req_body['params'].push(options)
        if position is not None:
            self.req_body['params'].push(position)
        return json.dumps(self.req_body)

    def tellStatus(self, gid, fields=None):
        self.req_body['id'] = 'tell_status_query'
        self.req_body['method'] = 'aria2.tellStatus'
        self.req_body['params'] = [gid]
        if fields is not None:
            self.req_body['params'].push(fields)
        return json.dumps(self.req_body)
