import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_001(self):
        print('test test1')

    def test_002(self):
        print('test test2')

    # @unittest.skip('asdf')
    def test_003(self):
        print('test test3')

    def tearDown(self):
        print('test over!')


class A(unittest.TestCase):
    def test1(self):
        print('test A1')

suite = unittest.TestSuite()
print(suite)
suite.addTest(Test('test_001'))
suite.addTest(Test('test_002'))
suite.addTest(Test('test_003'))
suite.addTest(A('test1'))
print(suite)
runner = unittest.TextTestRunner()
runner.run(suite)
