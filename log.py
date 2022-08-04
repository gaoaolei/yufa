import requests

url = "https://dsp-api-test.19ego.cn/qcj/api/log"
body = {
    "requestInfo": {
        "b": {
            "actId": 0,
            "advertId": "46",
            "aid": 0,
            "catId": 8,
            "catName": "land_page1",
            "env": None,
            "goodsId": 0,
            "goodsSource": 0,
            "appSource": 0,
            "goodsUrl": "",
            "pid": 0,
            "popup": 0,
            "rid": "",
            "sKey": "q83c921639dfb2ee5",
            "sid": 0,
            "ua": "",
            "uid": 0,
            "ajts": "3",
            "material": "29",
            "landPageIndex": "0",
            "index": 104
        },
        "d": {
            # "id": "8309a9a7e96c473280b16519c638a000",
            "id": "18888888888888888888888888880000",
            "os": "0"
        },
        "g": {
            "city": "unknow",
            "ip4": "172.31.10.1",
            "isp": "unknow",
            "province": "unknow"
        }
    },
    "code": 4001
}

for i in range(25):
    deviceId = body['requestInfo']['d']['id']
    body['requestInfo']['d']['id'] = str(int(deviceId) + 1)
    r = requests.post(url, json=body)
    print(r.text)
