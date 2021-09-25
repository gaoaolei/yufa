class Fib():
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):  # 可以index取值
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


# fib4 = Fib()
# for i in fib4:
#     print(i)
# print(fib4[5])

class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        else:
            return "没有该属性"

    def __setattr__(self, key, value):
        self.__dict__[key] = value  # 必须要将属性注册到dict中去

    def __delattr__(self, item):
        # del self.__dict__[item]
        # 或者
        super().__delattr__(item)


s = Student()
print(s.name)
s.score=99
print(s.score)
s.age = 30
print(s.age)
del s.age
print(s.age)


# 向量
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x,self.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(type(v1 + v2))
print(v1+v2)


# __call__   使实例可以直接调用    dir(obj)有__call__则说明是callale对象，可用callable（）检查为True

class A():
    def __call__(self, *args, **kwargs):
        return "nihao"
a = A()
print(a())


