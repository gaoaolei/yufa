# import paramunittest
# import unittest
# list = [(123,456),#{a':123,"b":456},
#         [123,45]]
# @paramunittest.parametrized(*list)
# class testMethod(unittest.TestCase):
#     def setParameters(self, a, b):
#         self.a = a
#         self.b = b
#     def setUp(self):
#         pass
#     def test001(self):
#         self.assertEqual(self.a, 123)
#     def test002(self):
#         self.assertEqual(self.b, 456)
#     def tearDown(self):
#         pass
#
# if __name__ == '__main__':
#     unittest.main()



import unittest

class testMethod(unittest.TestCase):

    def setUp(self):
        pass
    def test001(self):
        print(1)
    def test002(self):
        print(2)
    def tearDown(self):
        pass