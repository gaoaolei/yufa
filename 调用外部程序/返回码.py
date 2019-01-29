# _*_coding:utf-8_*_
# for windows
import os
returncode = os.system('dir')
print(returncode)            # 返回码为0表示正确调用了外部程序

# for linux
# echo $?     # 最简单的，其他的百度
print('----------------------分割线-----------------------')
import os
ret = os.system('mspaint')
if ret == 0:
    print('paint is opened')
else:
    print('paint open failed')


