#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('172.16.20.231', 7777)

sk = socket.socket()
sk.connect(ip_port)

sk.send('feihuaduo')

server_reply = sk.recv(1024)
print server_reply

sk.close()