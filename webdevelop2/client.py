#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall('yongzimuba')

server_reply = sk.recv(1024)
print server_reply

sk.close()