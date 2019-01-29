# file_object=open(file_name,access_mode='r')
# f=open('C:/Users/GaoAolei/Desktop/test','r')     #mode可缺省
f=open('C:/Users/GaoAolei/Desktop/test.txt','br')  # seek带参数时需要用二进制读取文件
print(f)
print(f.seek(3))
print(f.tell())
print(f.seek(4,1))
print(f.seek(1,2))
f.seek(0)
print(f.seek(1,2))
print(f.seek(0,2))   # 可以显示文件的总长度
######################################################################
#  seek的参数讲解
#  seek(x，y)   x表示offset，y=0表示从绝对开头位置起，此时y可以省略     x为负数时表示向左
#                            y=1表示从当前位置起
#                            y=2表示从绝对尾部位置起
######################################################################
f.seek(0)
print(f.read())
f.seek(0)
print(f.read(3))
f.seek(0)
print(f.readlines())       #readlines()返回的是列表
f.seek(0)
print(f.readlines(2))
f.seek(0)
f.close()              # 对文件操作完后必须关闭文件

# 文件打开的另一种方法     此种写法执行结束后会自动调用close()
with open('C:/Users/GaoAolei/Desktop/test1.txt','r') as f:
    content=f.read()
    index=f.tell()
print(content)
print(index)
# 打开多个文件
with open('C:/Users/GaoAolei/Desktop/test.txt','r') as rfile,open('C:/Users/GaoAolei/Desktop/test1.txt','w') as wfile:
    f=rfile.read()
    copy=wfile.write(f)             # 此例子实现了copy的功能


beforetax=[1,2,3,4,5]
aftertax=[0.9*x for x in beforetax if x>2]
print(aftertax)




