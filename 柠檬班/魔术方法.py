"""
1、通过装饰器实现单例模式，只要任意一个类使用该装饰器装饰，
那么就会变成一个单例模式的类。(面试真题)


2、请实现一个类，前五次创建对象，每次都可以返回一个新的对象，
第六次开始，每次创建，都随机返回前5个对象中的一个

3、自定义一个列表类型，实现对象可以之间可以 使用 -  来进行操作
# 要求：如果一个对象减去另一个对象，则把和被减对象中一样的数据给删除掉
# 如下：
li1 = MyList([11, 22, 33,22, 44])
li2 = MyList([1, 22])
res = li1 - li2
# res 打印的结果为[11,33,44]
"""


def decorator(cls):
    setattr(cls, '__instance', None)

    def wrapper(var):
        if not cls.__instance:
            cls.__instance = cls(var)
        return cls.__instance

    return wrapper


@decorator  # Single=decorator(Single)=wrapper
class Single(object):
    pass


print('--------------------------------------------------------')


class Demo(object):
    __instance_list = []

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if len(cls.__instance_list) < 5:
            obj = object.__new__(cls)
            cls.__instance_list.append(obj)
            return obj
        else:
            import random
            index = random.randint(0, 4)
            return cls.__instance_list[index]


print(Demo())
print(Demo())
print(Demo())
print(Demo())
print(Demo())
print(Demo())
print(Demo())
print(Demo())

print('--------------------------------------------------------')


class MyList(list):
    def __init__(self, args):
        super().__init__(args)

    def __sub__(self, other):
        return list(set(self) - set(other))


li1 = MyList([11, 22, 33, 22, 44])
li2 = MyList([1, 22])
print(li1)
print(li2)
print(li1 - li2)
open()
