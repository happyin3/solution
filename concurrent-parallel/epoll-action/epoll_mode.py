# -*- coding: utf-8 -*-

import socket
import select


HOST = '127.0.0.1'
PORT = 8001
BUFFER_SIZE = 1024

# 生成socket，绑定ip端口
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)


def epoll_mode():
    running = True
    epoll = select.epoll()

    # 注册epoll读
    epoll.register(server.fileno, select.EPOLLIN)
    # 保存链接文件描述符和链接的对应关系
    conn_list = {}
    while running:
        try:
            # 开始执行epoll
            events = epoll.poll(1)
        except Exception as e:
            break

        if events:
            for fileno, event in events:
                # 如果是新链接，则accept，并将新链接注册到epoll中
                if fileno == server.fileno():
                    conn, addr = server.accept()
                    conn.setblocking(0)
                    epoll.register(conn.fileno(), select.EPOLLIN)
                    conn_list[conn.fileno()] = conn

                # 如果是其他的可读链接，则获取到链接，recv数据，如果是
                # \n，则close，并冲epoll中unreguster掉这个文件描述符
                elif event == select.EPOLLIN:
                    data = conn_list[fileno].recv(BUFFER_SIZE)
                    if data.startswith('\n'):
                        conn_list[fileno].close()
                        epoll.unregister(fileno)
                        del(conn_list[fileno])
                    else:
                        conn_list[fileno].send(data)

    server.close()
