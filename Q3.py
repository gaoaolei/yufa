def f():
    import sys
    import paramiko
    from paramiko_expect import SSHClientInteraction
    import requests
    import json
    import time
    import hmac
    import hashlib
    import base64
    import urllib.parse

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

    def output_func(msg):
        json_list = []
        json_list.append(msg)
        URL = "https://oapi.dingtalk.com/robot/send?access_token=9228b415ed650324c31f22c6f25ed573cc634e95144c6d0ca01d77255358cce8"
        import time
        timestamp = str(round(time.time() * 1000))
        secret = "SEC7b025dd4ba172ac8a14fe4b6afa1e057182d25796413d27f5f79e6b0b81c9add"  # SEC开头的
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        import hmac
        import hashlib
        hmac_code = hmac.new(secret_enc, string_to_sign_enc,
                             digestmod=hashlib.sha256).digest()
        import urllib
        import base64
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        webhook = URL + "&timestamp=" + timestamp + "&sign=" + sign
        headers = {'Content-Type': 'application/json'}
        data = {
            "msgtype": "text",
            "text": {
                "content": msg,
            },
        }
        x = requests.post(url=webhook, data=json.dumps(data), headers=headers)
        # print(x.json())
        # if x.json()["errcode"] == 0:
        #    return True
        # else:
        #    return False
        # dingtalk_warning(msg)
        import sys
        sys.stdout.flush()

    # def conn_tail(ip,path):
    ip =''
    path =''
    hostname = ip
    port = 22
    username = "root"
    password = "gyjxwh.com!"
    client = None
    import paramiko
    client_tmp = paramiko.SSHClient()
    client_tmp.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client_tmp.connect(hostname, port, username, password, compress=True)
        client = client_tmp
    except:
        client = None
    from paramiko_expect import SSHClientInteraction
    interact = SSHClientInteraction(client, timeout=10, display=False)
    interact.send('tail -f %s' % path)
    interact.tail(output_callback=output_func)


import threading

threading.Thread(target=f).start()
