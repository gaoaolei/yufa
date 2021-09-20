import urllib3
urllib3.disable_warnings()  # 忽略警告
import pytest


@pytest.mark.skip(reason="忽略")
def test_vip_01(login_android_fixture):
    s = login_android_fixture
    url = "https://xiaoshuo.wtzw.com/api/v1/user/get-role-adv-vip-info-for-android?apiVersion=20190309143259-1.9"
    r = s.get(url=url, verify=False)
    res = r.json()
    assert res['data']['users']['nickname'] == "七猫书友_040253100555"


def test_vip_7day(login_android_fixture):
    s = login_android_fixture
    url = "https://xiaoshuo.wtzw.com/api/v1/pay/vip-pay?type=2&money=3&platform=1&apiVersion=20190309143259-1.9"
    r = s.get(url=url, verify=False)
    res = r.json()
    print(res)
