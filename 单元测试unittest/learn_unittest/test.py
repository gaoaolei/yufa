import unittest

from test2 import *
from test1 import *
import test1

if __name__ == "__main__":
    # 一、 不使用suite，main()--TestProgram()--runtest()---TextTestRunner().runner(cae/suite)
    # unittest.main()    # 没有TestSuiteClass，只有TestCaseClass
    # 二、 使用suite，定义时直接传入TestSuite(tests=()),初始化中会调self.addTests(tests)
    # suite1 = unittest.TestSuite(map(TestUserLogin, ["test_001", "test_login"]))  # TestSuiteClass
    # suite2 = unittest.TestSuite(map(TestUserLogin1, ["test_001", "test_login"]))  # TestSuiteClass
    # suite1 = unittest.TestSuite()
    # print(type(suite1))
    # for i in suite1:
    #     print(i)
    # unittest.TextTestRunner().run(suite1)  # 可以运行，run接受case或suite
    # unittest.TextTestRunner().run([suite1, suite2])  # 不可以运行，run接受case或suite，不接受list
    # unittest.TextTestRunner().run(unittest.TestSuite([suite1, suite2]))  # 可以运行，unittest.TestSuite([suite1,suite2])等
    #  于new了一个suite实例，里面是list，含两个子suite； def __init__(self, tests=()):TestSuite可接受任意类型
    # 三、 使用suite的adds函数添加用例
    # suite3 = unittest.TestSuite()
    # suite3.addTests(map(TestUserLogin, ['test_001', 'test_login']))
    # suite3.addTests(map(TestUserLogin, ['test_001']))
    # 四、使用suite的add函数添加用例
    # suite4 = unittest.TestSuite()
    # suite4.addTest(TestUserLogin("test_001"))
    # print(suite4)
    # unittest.TextTestRunner().run(suite4)
    # # 五、unittest.makeSuite
    # suite5 = unittest.makeSuite(TestUserLogin, prefix='test')
    # 六、findTestCases
    # suite6 = unittest.findTestCases(test1, prefix='test')
    # 如果用的是本py，不能直接使用test，必须采用下法__name__
    # module = __import__(__name__)
    # print(module)
    # # suite6 = unittest.findTestCases(module, prefix='test')
    # print(suite6)
    # print(suite6)
    # 七、loadTestsFromTestCase(self, testCaseClass)    return loaded_suite
    # suite7 = unittest.TestLoader().loadTestsFromTestCase(TestUserLogin3)
    # print(suite7)
    # unittest.TextTestRunner().run(suite7)
    # 八、
    # suite8 = unittest.TestLoader().loadTestsFromModule(test1)
    # 但是下面写法也可以，不懂
    # suite9 = unittest.TestLoader().loadTestsFromModule(test1.TestUserLogin())
    # print(suite9)
    # unittest.TextTestRunner().run(suite8)
    # 九、需要引号 loadTestsFromName
    suite10 = unittest.defaultTestLoader.loadTestsFromName('test1')
    suite11 = unittest.TestLoader().loadTestsFromName('test1.TestUserLogin')
    suite12 = unittest.TestLoader().loadTestsFromName('test1.TestUserLogin.test_login')
    # print(suite10)
    # print(suite11)
    # print(suite12)
    # 十、需要引号 loadTestsFromNames
    # suite13 = unittest.TestLoader().loadTestsFromNames('test1')
    # test_case = unittest.TestLoader().loadTestsFromNames('test1')
    # suite15 = unittest.TestLoader().loadTestsFromNames('test1.TestUserLogin.test_login')
    # print(suite13)
    # print(test_case)
    # print(suite15)
    # 十一、discover(start_dir)
    # suite16 = unittest.TestLoader().discover(r"C:\Users\Administrator\Desktop\LocalCode\七猫接口监控\a")
    # print(suite16)
    sui = unittest.TestSuite()
    a = TestUserLogin("test_login")  # 具体用例的表示方式
    b = TestUserLogin("test_001")
    sui.addTests((a, b))
    print(sui)
    # print(unittest.TestSuite([TestUserLogin("test_001")]))
    # unittest.TextTestRunner().run(unittest.TestSuite(unittest.TestSuite(unittest.TestSuite(suite))))

    # 总结：不手动修改用例的加载时，就不会产生套件，只能使用unittest.main()运行
    # 使用套件的时候，new的时候一定是可迭代的对象，不然会报错
    # 不显示使用套件的时候，可以用TestLoader加载用例
    # suite可无限嵌套