#!/usr/bin/env python
# coding:utf-8
from wsgiref.simple_server import make_server
from jinja2 import Template
import mysqltest

def index():
    # return 'welcome you!'

    # f = open('index.html','r')
    # data = f.read()
    # return data

    # template = Template('Hello {{ name }}!')
    # result = template.render(name='John Doe')
    # result = result.encode('utf-8')
    # return result
    # 数据处理
    name = mysqltest.check('select nickname from user where id=1062103420')
    result = mysqltest.check('select nickname from user limit 10')
    user_list = []
    for item in result:
        user_list.append(item[0])

    f = open('index2.html')
    result = f.read()
    template = Template(result)
    data = template.render(name=name[0][0], user_list=user_list) # --->shujuku
    return data.encode('utf-8')

def login():
    # return 'please login with username and password!'
    f = open('login.html', 'r')
    data = f.read()
    return data

def routers():
    urlpatterns = (
        ('/index/', index),
        ('/login/', login),
    )
    return urlpatterns


def RunServer(environ, start_response):
    print environ
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == url:
            func = item[1]
            break
    if func:
        return func()
    else:
        return '404 not found'


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()