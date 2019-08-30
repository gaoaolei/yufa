import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start')
    def test_001(self):
        print('Test_001')
    def test_002(self):
        print('Test_002')
    @unittest.skip('asdf')
    def test_003(self):
        print('Test_003')
    @classmethod
    def tearDownClass(cls):
        print('test over!')

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Test('test_001'))# 好像不起作用，默认全部自动添加进来了
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
