f=open('C:/Users/GaoAolei/Desktop/test1.txt','w')        # open已存在的文件 会立马清空该文件，所以一定要小心！！！、
f.write('daiqiaozhen')
f.flush()                       # 将写的内容从buffer写到磁盘
f.close()

# 追加内容
f=open('C:/Users/GaoAolei/Desktop/test1.txt','a')        # 不清空文件
f.write('woaini')