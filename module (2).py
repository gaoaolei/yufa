# 模块中的标志符（identifier）：变量，函数，类
import time
import os
print(time.strftime('%Y_%m_%d %H:%M:%S'))
time.sleep(1)
print(0)
time.sleep(1)
os.system('calc')
import sys
print(sys.builtin_module_names)        # 找到内置库（直接包含在解释其中，不需要去寻找）
print(sys.path)
print(os.__file__)


