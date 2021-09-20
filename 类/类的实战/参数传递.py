from unittest import TestCase, main as unittest_main

"""怎么使用前一个用例修改后的参数"""

class TestSimpleFoo(TestCase):
    foo = 'bar'

    def test_a(self):
        self.assertEqual(self.foo, 'bar')
        TestSimpleFoo.foo = 'can'    #****************

    def test_f(self):
        self.assertEqual(self.foo, 'can')


if __name__ == '__main__':
    unittest_main()