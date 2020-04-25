class Student():
    pass


# 动态给实例添加属性
s=Student()
s.name = 'gaoaolei'
print(s.name)

# 动态给实例添加方法
from types import MethodType
def f(self):
    print('这是实例方法')
s=Student()
s.f = MethodType(f,s)


# 动态（其实无所谓动静）给类添加属性，在类中添加类属性即可

# 动态给类添加方法
def func(self):
    print('这是类方法')
Student.func = func
s=Student()
s.func()