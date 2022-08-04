# 第一种传参，装饰器接受参数，缺点：只能对不同的参数传参数，不能对同一个函数传不同的参数
def log(var):
    def decorator(f):
        def wrapper(*args,**kw):
            return f(*args,**kw)+var
        return wrapper
    return decorator
@log(100)
def addd(*args,**kw):
    a = 0
    for i in args:
        a = a + i
    return a
@log(101)
def addd2(*args,**kw):
    a = 0
    for i in args:
        a = a + i
    return a
print(addd(1,2,3))
print(addd2(1,2,3))

# 第二种传参，被装饰的函数接受参数，较第一种灵活
def log1(f):
    def wrapper(*args,**kw):
        def chuancan(var=200):
            return f(*args,**kw)+var
        return chuancan
    return wrapper
@log1
def addd3(*args,**kw):
    a = 0
    for i in args:
        a = a + i
    return a
print(addd3(1,2,3)())
@log1
def addd4(a,b):
    return a+b
print(addd4(1,2)(100))