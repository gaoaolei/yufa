import time
import hmac
import hashlib
import urllib.parse
import base64
import requests
import json
import os
def dingtalk(message, atMobiles):

    url = "https://oapi.dingtalk.com/robot/send?access_token=320f245f6eef3c170a76d80532e7bb5bb07115b0ed4f4bc46ad5f6b51c14033c"
    secret = "SECc1b3c2cb35ef10ff5479ac5ef0d7ad253373bfc61d3ad861799cd147ef8e41c1"

    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    webhook = url + "&timestamp=" + timestamp + "&sign=" + sign
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": message,
        },
        "at": {
            "atMobiles": [
                *atMobiles
            ],
            "atUserIds": [

            ],
            "isAtAll": False
        }
    }
    send_result = requests.post(url=webhook, data=json.dumps(data), headers=headers)
    if send_result.json()["errcode"] == 0:
        return True
    else:
        return False
import sys
import traceback

def ding(owner):
    def bibao(f):
        def wrapper():
            try:
                return f()
            except:
                e = traceback.format_exc()
                dingtalk(e, [owner])
                raise e
        return wrapper
    return bibao


@ding(15171001790)
def aa():
    return 1/0




if __name__ == '__main__':
    # dingtalk("hello world!", [15171001790])
    aa()
