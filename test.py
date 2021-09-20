import requests


s = requests.session()

# ********************************获取token*************************
url = "https://xiaoshuo.wtzw.com/api/v1/login/index"

body = {
    "cancell_check": "1",
    "encrypt_phone": "ghfnNe0wgI0EAh9=",
    "gender": "2",
    "open_push": "0",
    "type": "1",
    "verify": "4321",
    "sign": "0ee145136a247c3344bd870e38b54f79"
}
s.headers = {
    "net-env": "1",
    "channel": "unknown",
    "is-white": "1",
    "platform": "android",
    "app-version": "60680",
    "reg": "2362397170",
    "application-id": "com.kmxs.reader",
    "AUTHORIZATION": "eyJhbGciOiJSUzI1NiIsImNyaXQiOlsiaXNzIiwianRpIiwiaWF0IiwiZXhwIl0sImtpZCI6IjE1MzEyMDM3NjkiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2MzM0MDc2OTMsImlhdCI6MTYzMjExMTY5MywiaXNzIjoiaHR0cHM6Ly94aWFvc2h1by53dHp3LmNvbS9hcGkvdjEvbG9naW4vdG91cmlzdCIsImp0aSI6InRvdXJpc3QiLCJ1c2VyIjp7InVpZCI6MTk2NTI0ODYxLCJuaWNrbmFtZSI6Iua4uOWuojA5MjA1MDEwMTU1MSIsImltZWkiOiIiLCJ1dWlkIjoiZmZmZmZmZmYtZGRhYS1iYjYxLTAwMDAtMDAwMDAwMDAwMDAwIiwiZGV2aWNlSWQiOiIyMDIxMDkxNDE2MDkyMWJmNmNkNGIxMzUwYjQxY2E2NDU4Y2U0ZWEyYTExZWY1MDFhYTkxNjMwOTg4NGVlMyIsInJlZ1RpbWUiOjE2MzIxMDY3NTQsInZpcEV4cGlyZUF0IjowLCJzbV9pZCI6IjIwMjEwOTIwMTA1NzM1YzQ2YTFmOTdhOGM2MDkwY2NjNmQxMGZiMDZlMmZkZmMwMGU2ZjA1ZmNmYzVmMjIwIiwibnV0IjowLCJpZnUiOjAsImlzX3JiZiI6MCwiYWN0X2lkIjowLCJiaW5kX2F0IjowLCJ0aWQiOiJEdUR5bGFlSXZ1dE9WZFo2MHFWbENsQTRNQko4UExQZEw5SmEyRlJiSThKOGRUQkVGVzBFZVlONnlPQlRWaWMzYnUzUFpCd1JRalJTSkl3OTJiSW1OUnR3IiwidF9tb2RlIjoxfX0.U9_cHYz_hcAWoPCKXd4OTucGTQe0ykfpTo32USVcfcRe0sfcqtFJmmoWRlBnUjgxQbUfE9lyMYx6yn51PWO5Uo_gSlsLjm6KTT0UOJ8DvejuG5J1gPy8zpkvS6STYAcRcPN8IB6JS49Z_FVyVlLiWzeaYvNxAmvH0mFb2LMOUEk",
    "qm-params": "cLGUuq2-HTZ5pzpzpzpzpz4Qpykx43U54T4nth9wgI9QgI9wgI9wgI9wgI9wH5w5pyRlmqN2tq2-HTZ5gT9Lgh9YghFnNT9YgTo5pTpTpIk5ghgUgyHMgqNxNTFUAyN2NyRxgz0ngqRzNh9n4q0Ygh4egI-rAIk2phg5taGQ4qg5A5GINI1ogeZYkTZlNIZUFTZEk5HjHSNYOLUlpCH5A5HngaHjHSkLuCNMpqFQmqF5A5G0ufkYByo23CpUu0JqpoZlg_oqB0NjFhkNF-Zrf0nFp0wY3z0Lk2G53hxiAykfF-RyResopR2ANS28F2kqmqge4Sfefo1auUGkm2Gh3-2EAhG53qUAfSkEH5w5mqU2m3HWH5HjHzUDpyRjHTZ5f0Nshh9wH5w5uln5tq2Qpq-5A5H5taGEByHQuq2-HTZ5FTuaNIxIg04ng-4EN0pIFTKEFeHUF-FlFT-UN-FENhgEpI4ngqfLgzHM4hG5gT-LgyFE4qk24T9E4eOUgIgYpaHjHzNjmqR7uaU1paHWHTpTNe-npI-eNhp54THEpyg5taG5Ozo7paHWH-JFf0d5taGD4q2-HTZ5FTuaNIxIg04ng-4EN0pIFTKEFeHUF-FlFT-UN-FENhgEpI4ngqfLgzHM4hG5gT-LgyFE4qk24T9E4eOUgIgYpaGJ",
    "sign": "af8ca2678a826be33e0f3a1b10ef6cdf",
    "QM-it": "1632106659",
    "QM-uaf": "20210920-196524861",
    "QM-ii": "3670268927",
    "no-permiss": "1",
    "User-Agent": "webviewversion/0",
    "Content-Type": "application/x-www-form-urlencoded",
    # "Content-Length": "124",
    "Host": "xiaoshuo.wtzw.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "x-forwarded-for": "218.195.219.255"
}


def login_token():
    """登录后获取token"""
    r = s.post(url, body, headers=s.headers)
    token = r.json()['data']['token']
    # 写死，不然每次登录都会变，需要重算sign，很麻烦
    token = 'eyJhbGciOiJSUzI1NiIsImNyaXQiOlsiaXNzIiwianRpIiwiaWF0IiwiZXhwIl0sImtpZCI6IjE1MzEyMDM3NjkiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2MzM0MTE5OTMsImlhdCI6MTYzMjExNTk5MywiaXNzIjoiaHR0cHM6Ly94aWFvc2h1by53dHp3LmNvbS9hcGkvdjEvbG9naW4vaW5kZXgiLCJqdGkiOiI0YWIyNzk5YTliNzBjZDg2MjRjNjk1MTA4MDJiNTYzMSIsInVzZXIiOnsidWlkIjoxMDUyNzMwMDIsIm5pY2tuYW1lIjoi5aW95ZCs55qE5pi156ewIiwiaW1laSI6IiIsInV1aWQiOiJmZmZmZmZmZi1kZGFhLWJiNjEtMDAwMC0wMDAwMDAwMDAwMDAiLCJkZXZpY2VJZCI6IjIwMjEwOTE0MTYwOTIxYmY2Y2Q0YjEzNTBiNDFjYTY0NThjZTRlYTJhMTFlZjUwMWFhOTE2MzA5ODg0ZWUzIiwicmVnVGltZSI6MTU5NjYyNTg4NywidmlwRXhwaXJlQXQiOjE2NjE5NjE2MDAsInNtX2lkIjoiMjAxODExMDgxMzQ2NDNhZDkzNzIzNDgxZmZmMzY5MjBmMTdhYzRiYTRhMGRlMjAxMjZjODRhNjEwNTQzNzkiLCJudXQiOjAsImlmdSI6MCwiaXNfcmJmIjowLCJhY3RfaWQiOjAsImJpbmRfYXQiOjAsInRpZCI6IkR1RHlsYWVJdnV0T1ZkWjYwcVZsQ2xBNE1CSjhQTFBkTDlKYTJGUmJJOEo4ZFRCRUZXMEVlWU42eU9CVFZpYzNidTNQWkJ3UlFqUlNKSXc5MmJJbU5SdHciLCJ0X21vZGUiOjJ9fQ.YS7iwmq9ajGKcJ8iqzKF9WmKxNp_-58pJd55E_oZNtPj3ErVUe1AjD2ana6AY79WXpddFAm7nrn3U_T5m_HryoCKbHZLvxaIh8PZ3idhTt5HhnwIKXLlEYSuXW235o1u-A3MgRqZGVQJs-ulK9a_sZjNPLpKVl6Gad765ReSWHw'

    return token
# ********************************获取token*************************

# 替换token和sign
s.headers.update({"AUTHORIZATION":login_token()})
s.headers.update({"sign":"4cb8b698138c10768261d184c7c1508f"})
h = {"sign1":"4cb8b698138c10768261d184c7c1508f1"}

def my_center():
    url = "https://xiaoshuo.wtzw.com/api/v2/user/my-center?down=1&act_time=1632106752&latest_read_time=&read_preference=2&sign=1253df5f09c0b5223adc1c5d196d515d"
    r = s.get(url,headers = h)        #  **************************有了session就不用再传headers了************************
    return r.json()


print(my_center())
