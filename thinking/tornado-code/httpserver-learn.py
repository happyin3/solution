'''Tornado httpserver.py 源码学习

# 知识图谱

- __future__
- 多继承

# 参考
'''

__author__ = 'happyin3 (happyinx3@gmail,com)'


class HTTPServer(TCPServer, Configurable, httputil.HTTPServerConnectionDelegate):

    def __init__(self, *args, **kwargs):
        pass

    def initialize(self, *args, **kwargs):
        pass

    @classmethod
    def configurable_base(cls):
        return HTTPServer

    @classmethod
    def configurable_default(cls):
        return HTTPServer

    @gen.coroutine
    def close_all_connections(self):
        pass

    def handle_stream(self, stream, address):
        pass

    def start_request(self, server_conn, request_conn):
        pass

    def on_close(self, server_conn):
        pass


class _CallableAdapter(httputil.HTTPMessageDelegate):
    def __init__(self, request_callback, request_conn):
        pass

    def headers_received(self, start_line, headers):
        pass

    def data_received(self, chunk):
        pass

    def finish(self):
        pass

    def on_connection_close(self):
        pass


class _HTTPRequestContext(object):
    def __init__(self, stream, address, protocol, trusted_downstream=None):
        pass

    def __str__(self):
        pass

    def _apply_xheaders(self, headers):
        pass

    def _unapply_xheaders(self):
        pass


class _ProxyAdapter(httputil.HTTPServerConnectionDelegate):
    def __init__(self, delegate, request_conn):
        pass

    def headers_received(self, start_line, headers):
        pass

    def data_received(self, chunk):
        pass

    def finish(self):
        pass

    def on_connection_close(self):
        pass

    def _cleanup(self):
        pass


HTTPRequest = httputil.HTTPServerRequest
