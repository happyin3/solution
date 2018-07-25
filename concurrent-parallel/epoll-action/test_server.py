# -*- coding: utf-8 -*-

import functools
import socket

from ioloop import IOLoop


io_loop = IOLoop()


def connection_ready(sock, fd, evens):
    print('call connect ready')
    while True:
        try:
            connection, addr = sock.accept()
        except Exception:
            raise
        connection.setblocking(0)
        handler_connection(connection, addr)


def make_sock():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    sock.bind(('', 8080))
    sock.listen(128)
    return sock


def handler_connection(conn, addr):
    callback = functools.partial(handler_read, conn)
    io_loop.add_handler(conn.fileno(), callback, io_loop.READ)


def handler_read(conn, fd, event):
    msg = conn.recv(1024)
    print('get msg %s' % msg)
    callback = functools.partial(handler_write, conn)
    io_loop.update_handler(conn.fileno(), callback, io_loop.WRITE)


def handler_write(conn, fd, event):
    response = '''HTTP/1.0 200 OK\r
        Date: Mon, 1 Jan 1996 01:01:01 GMT\r
        Content-Type: text/plain\r
        Content-Length: 13\r
        \r
        Hello, world!'''

    conn.send(response)
    conn.close()
    io_loop.remove_handler(conn.fileno())


if __name__ == '__main__':
    sock = make_sock()
    callback = functools.partial(connection_ready, sock)
    io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
    io_loop.start()
