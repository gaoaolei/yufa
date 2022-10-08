import time
import hmac
import hashlib
import urllib.parse
import base64
import requests
import json


def dingtalk_warning(message):
    URL = "https://oapi.dingtalk.com/robot/send?access_token=a50a32755dc18da8b83657d09fde72c087b33e21a5cf06f8979bf8764188d971"
    timestamp = str(round(time.time() * 1000))
    secret = "SECd0bd62a752b44cbcc59c94fd6cd07d16b4f0996ac14fc8a8c32b0c19eb71098d"  # SEC开头的
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc,
                         digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    webhook = URL + "&timestamp=" + timestamp + "&sign=" + sign
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": message,
        },
    }
    x = requests.post(url=webhook, data=json.dumps(data), headers=headers)
    # print(x.json())
    if x.json()["errcode"] == 0:
        return True
    else:
        return False


dingtalk_warning("hello world!")
