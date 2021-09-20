import requests
import urllib3
urllib3.disable_warnings()  # 忽略警告
import pytest
from .login import *


@pytest.fixture(scope="session")
def login_android_rj():
    """登录保持会话"""
    s = requests.session()
    login_android_rjuan(s)
    yield s
    s.close()


@pytest.fixture(scope="session")
def login_ios_rj():
    """登录保持会话"""
    s = requests.session()
    login_ios_rjuan(s)
    yield s
    s.close()


@pytest.fixture(scope="session")
def login_android_fixture_yyy():
    """登录保持会话"""
    s = requests.session()
    login_andriod_yyy(s)
    yield s
    s.close()

@pytest.fixture(scope="function")
def unlogin():
    """不需要登陆"""
    s = requests.session()
    yield s
    s.close()





