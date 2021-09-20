import requests
import urllib3
urllib3.disable_warnings()  # 忽略警告

"""提供登录方法"""

def login_android_rjuan(s):
    """
    android登录 - phone：17501670417； 验证码：4321
    :param s: s = requests.session()
    :return: r.json，请求后的响应为json格式，返回json数据
    """
    url = "https://xiaoshuo.wtzw.com/api/v1/login/index"
    body = {
        "cancell_check": "1",
        "encrypt_phone": "ghOUgI0lNe9MghO=",
        "gender": "2",
        "open_push": "1",
        "type": "1",
        "verify": "4321",
        "sign": "e79ef1c8fd542c9f48f487aa93ec1401"
            }
    header = {
        "net-env": "1",
        "channel": "unknown",
        "is-white": "0",
        "platform": "android",
        "app-version": "50900",
        "reg": "3030996534",
        "application-id": "com.kmxs.reader",
        "AUTHORIZATION": "",
        "qm-params": "cLGZ4CG-uloLp3U1paHWHzpzpzpzpzpztqo2AygQpyN2g3UzpzpztqpzpzpT4h9npzkzNaHjHSRUmqF5A5Gzpzpzpzpzp5U5phgUtqGx4qfQgI9wgaMwgI9wgI9wgI9wgI95taG-pCp14lfQmqF5A5HLgIHwgh0wNI0nNIfMNIKngy4npT4wpzgwpqo2pykTpzfEAhFYgzGTAh4EghHUgIo-pzHr4TKe4lGTpzgwN3HjHzUx4LHWHTFrATGIA-0wA-fEA-gEAT0rH5w5OE2etCp2O5HWHT-5taGMOSReuyR-tq2-HTZ5k_R8c3JtOlQDgMkUiEGIf0peu2ovtU9Lk0dvNekvBEpruyGUBqn3tMJDqI9n4UxIOUkfufMMh_FD3Toe3fkQpqpLfTGQOCslACFUOUo0OMQnuU2ttENkF3HjHz2Qpq-5A5H5taGQBlk2BaHWH2G2pyU1H0YDuyfKNLHjHSuj45U1BqR1HTZ5H5w5uln5tCR1paHWHTFrg-Nsg0fEFeOnAaHjHzNjmqR7uaU1paHWHTk-pqR2pzk-phgE4TgUghg5taG5Ozo7paHWHSx14qJQm3HjHzJxmqF5A5H56F==",
        "sign": "7353275ac6ed5c00440e75a2324a323d"
        }

    r = s.post(url=url, data=body, headers=header, verify=False)
    return r.json()


def login_ios_rjuan(s):
    """
    iOS登录 - phone：17501670417； 验证码：4321
    :param s: s = requests.session()
    :return: r.json，请求后的响应为json格式，返回json数据
    """
    url = "https://xiaoshuo.wtzw.com/api/v1/login/index"
    body = {
        "cancell_check": "1",
        "encrypt_phone": "ghOUgI0lNe9MghO=",
        "gender": "1",
        "sign": "dfe80cfac6e7f24bfd0c55208da08d16",
        "type": "1",
        "verify": "4321"
            }
    header = {
        "net-env": "1",
        "app-version": "4060000",
        "channel": "qi-appstore_wm",
        "application-id": "com.yueyou.cyreader",
        "platform": "ios",
        "sign": "3b0c34496a98b7c692b31a453703962e",
        "AUTHORIZATION": "",
        "qm-params": "cLGEByHQmqU2m3HWHTfwN04nF-4YthusNTfQN00wN3MYk-Hwtho0FefLge-lkI2aA3HjHzk2uz2Tp3U1paHWHTHwgT0wge9eghgwNTgeAI0M4qfepzozAhgEpIgw4eN-NTozgIx24qNT4efMNIgwgh-UNqR54egYpTgEgIu2H5w54ln1pqYMtq2-HTZ5H5w5uCR1paHWHTfwN04nF-4YthusNTfQN00wN3MYk-Hwtho0FefLge-lkI2aA3HjHSNYOLUlpCH5A5HnNarLH5w5BqJ-pqw5A5G1fyxDBzfrtI05taG5Ozo7paHWH-owOyn2H5w5u_GUOEk2paU1paHWH-FLmT0UhEuHNlge3yoomzdY3lRFcqGvh0JkF2GkORGrhhxAOfnCfRN_BIxVOUKrpaHjHz2Qpq-5A5HUgIkygfGyA3MEFh4UthksgIfQAfpagaMnk0gUgTgYN-FYFT-5taGQ4qg5A5H56F==",
        "reg": "3030996534",
        "is-white": "0"
        }

    r = s.post(url=url, data=body, headers=header, verify=False)
    return r.json()


def login_andriod_yyy(s):
    """
    android登录 - phone：18017875371； 验证码：4321
    :param s: s = requests.session()
    :return: r.json，请求后的响应为json格式，返回json数据
    """
    url = "https://xiaoshuo.wtzw.com/api/v1/login/index"
    body = {
        "cancell_check": "1",
        "encrypt_phone": "ghKwghOrNefeNe0=",
        "gender": "2",
        "open_push": "1",
        "type": "1",
        "verify": "4321",
        "sign": "2f911a6f025784417fab13ae2ac2b10e",
        "oaid":"50b6315892e8298a"
    }
    header = {
        "net-env": "1",
        "channel": "qm-xiaomi_lf",
        "is-white": "0",
        "platform": "android",
        "app-version": "51200",
        "reg": "3030996534",
        "application-id": "com.kmxs.reader",
        "AUTHORIZATION": "",
        "qm-params":"cLGZ4CG-uloLp3U1paHWHT9wgI9wgI9wth0e4zHQgIKngLUzpzpztqpzpzp2pT9U4qgM43HjHSRUmqF5A5HwgI9wgI9wgaMEgTuTtqFnNh9QgI9wgaMwgI9wgI9wgI9wgI95taG-pCp14lfQmqF5A5HLgI0Ygh9wAh0wghgnNlfrge9EpToTpTOepzp5NIKl4q4rgqHUAhgl4egM4TfLgIo-pT9YAIOMAIfrNIKep5HjHzUx4LHWHTOwA-GaA-fYA-oyATRyATR0H5w5OE2etCp2O5HWHT0wH5w5u_GUOEk2paU1paHWH-kUqfN1B_sAhS1pRyZYR-xLqo1rghuDB2GNAfxatU1qg0Q3RR2MkSNYte2URzUnh-nmfo1VBlntpUxvO0Yjgy-Mpfuj4fRigMkpm0ommMJaNS24OMkvff05taG1BqR1HTZ5H5w5BqJ-pqw5A5GN339rH0n1uyf5taGEByHQmqU2m3HWH5HjHSuj45UUmqF5A5HUgyHlge0UAI-LphKLAhxxH5w54ln1pqYMtq2-HTZ5pIfegh2-pIgwNe22NyfwgLHjHzGL4qY-HTZ5qy2xBlU1H5w5Blo1paHWHTfw4T4eghfrAhG2AIHYAy056F==",
        "sign": "6e069c9b55a45d8df87f93d1660150fb"
    }

    r = s.post(url=url, data=body, headers=header, verify=False)
    return r.json()


if __name__ == '__main__':
    s = requests.session()
    # print(login_android_rjuan(s))
    # print(login_ios_rjuan(s))
    print(login_andriod_yyy(s))

