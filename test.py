"""以联想电脑的galintercace_adv为基础，讲解如何实现用例的并发执行"""
from BeautifulReport import BeautifulReport

"""
1.工具：模块tomorrow的threads
2.如何使用：run()方法上加threads的装饰器@threads(5)  5表示5个子线程
3.run()既可以传case，应该也可以传suite，但如果suite的个数<线程数，可能有的线程没有任务，达不到高效
4.报告要区分，否则只会覆盖成最后一条case的结果，但区分了报告又太多了，怎么办？
5.用例之间是有数据一致性问题，待深究？
6.传case或suite的时候，一定注意传正确，很多时候suite会嵌套很多层suite，需要提取出来，如何提取？
        for i in suite:
            print(i._tests)
"""

import getpathInfo, time
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
from common import configEmail
from tomorrow import threads

path = getpathInfo.get_Path()


class AllTest():
    def __init__(self):
        self.caseFile = os.path.join(path, 'testCase')
        self.caseListFile = os.path.join(path, 'caselist.txt')
        self.caseList = []

    def set_case_list(self):
        fb = open(self.caseListFile, 'r')
        for value in fb.readlines():
            value = value.rstrip('\n')    # 防止caselist中回车跳行，导致\n != '',会产生空，导致set_case_suite中多出discover
            if value and not str(value).startswith('#'):
                self.caseList.append(str(value).replace('\n', ''))
        fb.close()
        return self.caseList

    def set_case_suite(self):
        caseList = self.set_case_list()  # 需要运行的用例名
        list = []
        for case in caseList:
            case_name = case
            # 批量加载用例，参数1为用例存放路径，2为用例文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            list.append(discover)
        return list

    # @threads(8)
    # def run(self, case, n):
    #     result = os.path.join(getpathInfo.get_Path(), 'result', 'report%s.html' % n )
    #     with open(result, 'wb') as f:
    #         runner = HTMLTestRunner(stream=f,
    #                                 title='接口测试结果',
    #                                 description='以下为七猫免费小说接口测试结果清单',
    #                                 verbosity=2)  # 这里面包含写内容了
    #         runner.run(case)

    @threads(8)
    def run(self, case, n):
        reportpath = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')
        result = BeautifulReport(case)
        result.report(reportpath)

if __name__ == '__main__':
    ins = AllTest()
    # all_case = unittest.TestSuite(ins.set_case_suite())
    all_case = ins.set_case_suite()
    print('================================')
    suite = all_case[0]
    a = None
    for i in suite:
        a = i._tests
    # print(a)

    for i, j in zip(a, range(len(a))):
        ins.run(i,j)
