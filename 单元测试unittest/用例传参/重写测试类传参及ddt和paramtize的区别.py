import unittest

"""
unittest默认不太支持用户取传参的，但实际应用中往往需要传参，本文介绍测试类传参的三个方法：
1.parameterise
2.ddt
3.本文，重写测试类
"""


class TestReport(unittest.TestCase):  # 创建测试类，unittest.TestCase运行时，默认运行该类下所有的def方法，一个def视作一条用例
    def __init__(self, testMethodName, param):  # 业务处理上需要传递一个参数param进来
        super(TestReport, self).__init__(
            testMethodName)  # 重新构造unittest.TestCase类的主函数，由于重写了__init__方法，需要传递用例的方法名称让unittest.TestCase类知道现在运行的是哪条def用例
        self.param = param  # 将业务参数param赋值给TestReport类，就可以在case1，case2中使用了

    @classmethod
    def setUpClass(cls):
        print("setup")

    def test_case1(self):
        print(self.param)
        # pass

    # @unittest.skip("wu")
    def test_case2(self):
        print(self.param)


testLoader = unittest.TestLoader()
testMethodNames = testLoader.getTestCaseNames(TestReport)  # 获取测试类的所有def方法，传递到测试类中
testSuite = unittest.TestSuite()
for i in [1, 2, 3]:
    for testMethodName in testMethodNames:
        testCase = TestReport(testMethodName, i)
        testSuite.addTest(testCase)


unittest.TextTestRunner().run(testSuite)

# 一定要以python文件形式运行，不要用unittest方式运行





cls.a=100
print(self.a)

# 结果为100

setupclass
参数化
setup
1001
测试结束
参数化
setup
50851
测试结束
参数化
setup
unknown
测试结束
setupclass
参数化
setup
1002
测试结束
参数化
setup
50700
测试结束
参数化
setup
qm-vivo_lf
测试结束
setupclass
参数化
setup
1003
测试结束
参数化
setup
50600
测试结束
参数化
setup
qm-oppo_lf
测试结束
参数化
setup
1004
测试结束
参数化
setup
41080
测试结束
参数化
setup
a
测试结束

其中setParameters加不加@classmethod都每次执行





paramter是先参数再用例
-0-testa
-0-testb
-1-testa
-1-testb
ddt是先用例再参数
testa-0
testa-1
testb-0
testb-1