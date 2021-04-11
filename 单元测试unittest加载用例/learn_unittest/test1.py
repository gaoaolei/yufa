import unittest

class TestUserLogin(unittest.TestCase):
    def setUp(self):
        print('测试开始前准备')

    def test_001(self):
        print("test_001")

    def test_login(self):
        print("login")

    def tearDown(self):
        print('测试结束')

class TestUserLogin1(unittest.TestCase):
    def setUp(self):
        print('测试开始前准备')

    def test_001(self):
        print("test_001")

    def test_login(self):
        print("login")

    def tearDown(self):
        print('测试结束')

if __name__ == "__main__":
    # unittest.main()    # 没有TestSuiteClass，只有TestCaseClass
    suite1 = unittest.TestSuite()      # TestSuiteClass
    print(suite1)


# testMethodNames = unittest.TestLoader().getTestCaseNames(TestUserLogin)  # 这个方法接收的确实是测试类



