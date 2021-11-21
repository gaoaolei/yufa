import flask
import json
from flask import request

server = flask.Flask(__name__)


# headers = request.headers

@server.route('/login',methods=['get','post'])
def login():
    username = request.values.get('name')
    pwd = request.values.get('pwd')
    if username and pwd:
        if username == 'xiaoming' and pwd == '111':
            result = {"code":200,'message':'登录成功'}
            return json.dumps(result,ensure_ascii=False)
        else:
            result = {'code':-1,'message':'账号密码错误'}
            return json.dumps(result,ensure_ascii=False)
    else:
        result = {"code":10001,'message':'参数不能为空'}
        return json.dumps(result,ensure_ascii=False),200,[('city','shanghai')]



# def center():
#     if 'token' in headers and headers["token"] == 'abcd':
#         result = {"account": 8888}


if __name__ == '__main__':
    server.run(debug=True,port=8000,host='127.0.0.1')