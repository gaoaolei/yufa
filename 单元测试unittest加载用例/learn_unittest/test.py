import unittest

from test2 import *
from test1 import *

if __name__ == "__main__":
    # 一、 不使用suite，main()--TestProgram()--runtest()---TextTestRunner().runner(cae/suite)
    # unittest.main()    # 没有TestSuiteClass，只有TestCaseClass
    # 二、 使用suite，定义时直接传入TestSuite(tests=()),初始化中会调self.addTests(tests)
    suite1 = unittest.TestSuite(map(TestUserLogin, ["test_001", "test_login"]))  # TestSuiteClass
    suite2 = unittest.TestSuite(map(TestUserLogin1, ["test_001", "test_login"]))  # TestSuiteClass
    # suite1 = unittest.TestSuite()
    print(type(suite1))
    for i in suite1:
        print(i)
    # unittest.TextTestRunner().run(suite1)  # 可以运行，run接受case或suite
    # unittest.TextTestRunner().run([suite1, suite2])  # 不可以运行，run接受case或suite，不接受list
    # unittest.TextTestRunner().run(unittest.TestSuite([suite1, suite2]))  # 可以运行，unittest.TestSuite([suite1,suite2])等
    #  于new了一个suite实例，里面是list，含两个子suite； def __init__(self, tests=()):TestSuite可接受任意类型
    # 三、 使用suite的adds函数添加用例
    suite3 = unittest.TestSuite()
    suite3.addTests(map(TestUserLogin, ['test_001', 'test_login']))
    suite3.addTests(map(TestUserLogin, ['test_001']))
    # 四、使用suite的add函数添加用例
    suite4 = unittest.TestSuite()
    suite4.addTest(TestUserLogin('test_001'))
    # 五、unittest.makeSuite
    suite5 = unittest.makeSuite(TestUserLogin, prefix='test')
    # 六、findTestCases
    module = __import__(__name__)
    print(module)
    suite6 = unittest.findTestCases('C:/Users/admin/Desktop/LocalCode/learn_unittest/test.py', prefix='test')
    # suite6 = unittest.findTestCases(module, prefix='test')
    print(suite6)
    # 七、TestLoader().loadTestsFromTestCase(testCaseClass)  return loaded_suite
    unittest.TestLoader().loadTestsFromModule(testCaseClass)  return loaded_suite
