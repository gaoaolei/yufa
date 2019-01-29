# _*_coding:utf_8_*_
import sys
print("script name is", sys.argv[0])      # 使用sys.argv[0]采集脚本名称
print(len(sys.argv))
if len(sys.argv) > 1:
    print("there are", len(sys.argv)-1, "arguments:")  # 使用len(sys.argv)-1采集参数个数-1为减去[0]脚本名称
    for arg in sys.argv[1:]:            #输出除了[0]外所有参数
        print(arg)
else:
    print("there are no arguments!")

    # 必须在交互环境中运行该脚本 2017.9.2
    # 给脚本附加参数时，参数之间空格隔开，不能用逗号
    # 了解更多，访问http://www.jb51.net/article/66610.htm

