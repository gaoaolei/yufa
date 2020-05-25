#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
# f = open('./ha.html','rb')
# content = f.read()
while True:
    print('server waiting...')
    conn,addr = sk.accept()
    client_data = conn.recv(1024)
    print(client_data)
    conn.sendall(b'\xe4\xb8\xad')
    conn.close()