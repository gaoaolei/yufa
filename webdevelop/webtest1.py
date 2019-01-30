
'''
WSGI接口：只要求web开发者实现一个函数，就可以响应http请求
'''
def HelloWorld(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1 style background:red>HelloWorld, I am python server</h1>']
# 2.7---str       3.6---byte
# 为什么return的内容必须是list？？？？？？？？？？？？？？？？？？？？？
# environ:一个包含所有HTTP请求信息的dict对象
# start_response:注意Header只能发送一次，也就是只能调用一次start_response()函数。start_response()函数接收两个参数，
# 一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示
# '''