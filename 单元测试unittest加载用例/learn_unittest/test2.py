import unittest


class TestUserLogin2(unittest.TestCase):
    def setUp(self):
        print('测试开始前准备')

    def test_001(self):
        print("test_001")

    def test_login(self):
        print("login")

    def tearDown(self):
        print('测试结束')


class TestUserLogin3(unittest.TestCase):
    def setUp(self):
        print('测试开始前准备')

    def test_001(self):
        print("test_001")

    def test_login(self):
        print("login")

    def tearDown(self):
        print('测试结束')

if __name__ == "__main__":
    unittest.main()
