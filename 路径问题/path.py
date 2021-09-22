"""
https://blog.51cto.com/wangwei007/1104940
"""

import os
print(__file__)
# 获取当前文件的绝真实路径
a = os.path.realpath(__file__)
print(a)
# 将路径劈开以获取文件的目录，从文件劈
b = os.path.split(a)
print(b[0])
# 将路径和文件拼接，得到新的文件路径
c = os.path.join(b[0],'testfile.txt')
print(c)
print(os.path.join(os.path.split(os.path.abspath(__file__))[0],'testfile.txt'))
print(os.path.join(os.path.dirname(os.path.abspath(__file__))),'testfile.txt')
# 判断路径是否存在
print(os.path.exists(c))
# 从扩展名劈
print(os.path.splitext(c))
# 获取文件的目录
print(os.path.dirname(c))
print(os.getcwd())

# 返回绝对路径
print(os.path.abspath(__file__))

# django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# realpath和abspath的区别：realpath返回非软连接路径


