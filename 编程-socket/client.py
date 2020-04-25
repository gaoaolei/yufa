#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall(b'\x11')   # 是以字节传递的，所以必须用字节数据

server_reply = sk.recv(1024)
print(server_reply)
print(server_reply.decode('utf-8'))

sk.close()