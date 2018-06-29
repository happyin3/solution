'''基于socket的服务器'''

__author__ = 'happyin3(happyinx3@gmail.com)'

from socket import socket, AF_INET, SOCK_STREAM


def tcp_handler(address, client_sock):
    '''
    :param address: <str> 客户端地址
    :client_sock: <socket> 连接套接字
    :return: <None>
    '''
    print('Got connection from {}'.format(address))

    while True:
        msg = client_sock.recv(1)
        print(msg)
        if msg == b'close':
            break
        client_sock.sendall(msg)
    print('sock close')
    client_sock.close()


def tcp_server(address, backlog=5):
    '''
    :param address: <str> 服务器地址
    :param backlog: <int>
    return: <None>
    '''
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)

    while True:
        client_sock, client_addr = sock.accept()
        tcp_handler(client_addr, client_sock)


if __name__ == '__main__':
    address = ('', 5000)
    tcp_server(address)
