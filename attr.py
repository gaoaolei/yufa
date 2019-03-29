# _*_coding:utf-8_*_
print dir('abc')                                # 获取对象的属性和方法
print len('abc')=='abc'.__len__()               # __.len__()实际是len()函数的方法，最终落到__len__()执行

class Myobject(object):
    def __init__(self,x):
        self.x=x
    def multi(self):
        return self.x*self.x
    def add(self):
        return self.x + self.y
obj=Myobject(8)
print obj.multi()
print hasattr(obj,'x')
print obj.x
print getattr(obj,'x')
setattr(obj,'y',19)
print obj.y
print getattr(obj,'y')
print obj.add()
# print getattr(obj,'z')
print getattr(obj,'z',404)

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
print readImage('E:\IMG_0057.jpg')
bygugyuguighui