"""IO"""
"""IO操作分为硬盘操作+内存操作

一、硬盘操作(存放的都是文件，主要是文件操作)

文件内容又分为str，num，list，dict等，其中str又分为文本文件和二进制文件
1.utf8格式的文本文件
f.read('r')

2.gbk格式的文本文件
f.read('r',encoding='gbk')

3.二进制文件(图片，视频)
f.read('rb')

4.变量（num，list，dict）关闭程序后就没了，想存到硬盘怎么办了？
import pickle
d={'a':123}
a = pickle.dumps(d)
f = open()
f.write(a)
或者直接写文件
pickle.dump(d,f)
其实，这个可以先将变量准成str存，读取的时候用eval()转回来
读就是load或loads

二、内存操作
数据读写不一定是文件，也可以在内存中读写，分为StringIO和BytesIO，即str和二进制数据
1.StringIO
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
hello world!

2.BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))

"""