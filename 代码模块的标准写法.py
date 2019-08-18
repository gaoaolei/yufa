# _*_coding:utf-8 _*_
# !/usr/bin/env python                                # 文件可以直接在unix，Linux，mac上运行
"""a test module"""                                       # 描述文件，这是一个测试模块
__author__='高傲雷'
import sys                                            # 导入内建模块sys
# print mystr.decode('utf-8').encode('gbk')           #传说中的使交互环境中的汉子不乱码的方法，但行不通，哭！！
args = sys.argv                                         # sys的默认至少有一个参数（列表argv），即脚本名称

def test():
    if len(args)==1:
        print('no argument')
    elif len(args)==2:
        print('one argument:,%s' %args[1])
    else:
        print('many arguments:%s' %args[1:])

if __name__ == '__main__':                              # 加了这一行后在其他地方（eg：call_module）导入时不成立，即不执行test()
     test()


