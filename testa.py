# class Demo:
#     def __init__(self,func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("功能扩展")
#         return self.func(*args, **kwargs)
#
#
# @Demo  # work = Demo(work)         work()=Demo(work)()=work
#
#
#
# def work(var):
#     print(var)
# #
# print(type(work(4)))
# class Demo:
#     def __init__(self,number):
#         self.number = number
#
#     def __call__(self, func):
#         print("扩展功能",self.number)
#         return func
#
# @Demo(3)  # work = Demo()(work)         work(4)=Demo()(work)(4)
# def work(*args,**kwargs):
#     print('asdfasdfafdsadsf')
#
# work(5)                # 这样写有个问题：没有调用就已经打印了扩展功能
#
#
#
# class Musen:
#     def __init__(self,number):
#         self.number =number
#     def __call__(self, func):
#         self.func=func
#         return self.run
#     def run(self,*args):
#         print('kuozhen')
#         return self.func(*args)
#
# @Musen(111)
# def work(x):
#     print('work执行---')
# work


# ====================================单例模式======================================
# class Single():
#     __instance = None
#
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             obj = object.__new__(cls)
#             cls.__instance = obj
#         return cls.__instance
#
#
# a = Single()
# Single.__instance = 1
# b = Single()
# c = Single()
# print(a, b, c)



def decorator(cls):
    setattr(cls, '__instance', None)

    def wrapper(var):
        if not cls.__instance:
            cls.__instance = cls(var)
        return cls.__instance

    return wrapper


@decorator  # Single=decorator(Single)=wrapper
class Single(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print('adsfasdf')

    def run1(self):
        print('adsfasdf')



