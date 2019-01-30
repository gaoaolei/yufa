# server
'''
python内置了一个wsgi服务器，模块为wsgiref
'''
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from webtest1 import HelloWorld

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
port = 9999
httpd = make_server('127.0.0.1', port, HelloWorld)
print('Congratulations to u Serving HTTP on port %s ...' % port)
# 开始监听HTTP请求:
httpd.serve_forever()