#!/usr/bin/env python
# coding:utf-8
import socket


def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")      # 服务端给客户端返回数据
    client.send("Hello, World")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # sock对象
    sock.bind(('127.0.0.1', 7777))      # 监听本机的8080端口
    sock.listen(10)                           # 最多接收5个连接

    while True:
        connection, address = sock.accept()     # 接收客户端请求
        handle_request(connection)
        print 'run in port 7777'
        connection.close()


if __name__ == '__main__':
    main()