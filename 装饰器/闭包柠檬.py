
"""----------------------------------------场景切入------------------------------------"""
# l=[]
# def res():
#     for i in range(5):
#         def f():
#             return i*i
#         l.append(f())
#     return l
# print(res())  #  [0,1,4,9,16]
"""---------------------------------如果我不需要立马执行函数，而只返回函数名，在需要的时候再进行调用---------------------------"""
# l=[]
# def res():
#     for i in range(5):
#         def f():
#             return i*i
#         l.append(f)           # 这里只是插入了函数名，没有传入i
#     return l
# # 此时l是一个列表，里面是函数，需要调用
# for f in res():               # 执行步骤：向l中插入5条f，此时i=4，再f()时，等于f(4)=16
#     print(f())      #[16,16,16,16,16]
# 可以看到结果全为16，因为调用的时候，数据i早就是4了，需要通过闭包将数据传进去并进行数据锁定
"""--------------------------------数据锁定----------------------------------------------------------------------"""
l=[]
def res():
    for i in range(5):
        def wrapper(i):          # 此时wrapper是一个闭包，形成了封闭作用域，并锁定i到对应的函数上
            def f():
                return i*i
            return f
        l.append(wrapper(i))    # 这里是直接调用，传入了f和i，所以闭包层下含函数名和数据（有点打包的意思）
    return l

# for f in res():
#     print(f())

"""***********************************由以上抽象出来就是一个最基本的闭包格式*****************************************
def bibao(x):
    def wrapper():
        return x
    return wrapper
# x就是内部引用的外部的局部变量，可以是变量，函数，类等任何对象

一、闭包的特征
1.函数嵌套
2.外层返回内层函数
3.内层有引用外部的非全局变量

二、闭包的作用
1.数据锁定
2.装饰器
***********************************由以上抽象出来就是一个最基本的闭包格式*****************************************"""


"""---------------------------------数据锁定再看一个例子-------------------------------"""
def bibao(*args):
    def wrapper():
        sum=0
        for i in args:
            sum=sum+i
        return sum
    return wrapper

datas = [(1,2,3),(11,22,33,44)]
l=[]
for i in datas:
    l.append(bibao(*i))
# for f in l:
#     print(f())
"""---------------------------------数据锁定再看一个高级点的例子-------------------------------"""
# class demo():
#     pass
#
# def login(self, x):   # 加了self就可以将这个函数设置成demo类的方法了，不然会没self报错
#     return "self的本来面目：{}--{}".format(self, x)
#
# def decorator(i):
#     def wrapper(self):
#         return login(self, i)
#     return wrapper
#
# datas = [11, 22, 33, 44]
# for i in datas:
#     # print()
#     object_name = demo  # 对象
#     method_name = "aa_{}".format(i)  # 属性名
#     # method_value = login  # 属性值
#     # 闭包，进行数据锁定
#     method_value = decorator(i)
#     setattr(object_name, method_name, method_value)  # 给对象设置属性
#     print(method_name)
#
# if __name__ == "__main__":
#     # print(demo.__dict__)
#     print(demo().aa_11())
#     print(demo().aa_22())
#     print(demo().aa_33())
#     print(demo().aa_22())
    # 现在login需要传值，unittest不支持传值，也不可能aa_11(123)这样传，因此需要闭包，包一层进行数据锁定

"""===============================装饰器作用示例，下文开始讲装饰器=================================="""
"""装饰器"""
"""被装饰对象前加"@装饰函数"即可实现一个装饰器，装饰器实质是一个语法糖，使用闭包来实现一些功能"""
"""
一、装饰器的实现
1.闭包
2.类
3.普通函数
可见装饰器不一定要闭包实现，只要是可调用对象（callable）都可以做装饰器，这个最后讲。
二、装饰器的作用
1.给对象做功能扩展
2.给对象做属性扩展（eg:ddt）
3.数据锁定
"""
"""----------------------------------最基础版-----------------------------------------"""
# def bibao(x):
#     def wrapper():
#         print("我是扩展的功能")
#         return x()
#     return wrapper
# @bibao              # @就是调用的意思，等于执行bibao(log)并将返回赋给log，log=bibao(log)=wrapper <==> log()=wrapper()
# def log():
#     return "hello"
# print(log())
"""----------------------------------被装饰函数有传参-----------------------------------------"""
# def bibao(x):
#     def wrapper(a):
#         print("我是扩展的功能")
#         return x(a)
#     return wrapper
# @bibao
# def log(var):
#     return var*var
# print(log(3))
"""----------------------------------被装饰函数传可变参数-----------------------------------------"""
# def bibao(x):
#     def wrapper(*args,**kwargs):
#         print("我是扩展的功能")
#         return x(*args,**kwargs)
#     return wrapper
# @bibao
# def log(var1,var2):
#     return var1*var2
# print(log(3,4))
"""----------------------------------装饰函数带参数-----------------------------------------"""
# def func(var):
#     def decorator(f):                               # 疑问：设计者为什么不直接将var放到decrator层，不就可以少一层吗？
#         def wrapper(*args, **kw):
#             print("我是扩展的功能")
#             return f(*args, **kw) + var
#         return wrapper
#     return decorator
# @func(11)
# def log(var1,var2):
#     return var1*var2
# print(log(3,4))
"""----------------------------------装饰函数带参数异型版-----------------------------------------"""
# def log1(f):
#     def wrapper(*args, **kw):
#         def chuancan(var=200):
#             return f(*args, **kw) + var
#         return chuancan
#     return wrapper
# @log1  # ---addd3 = log1(addd3)=wrapper-----addd3()=wrapper()=chuancan --------add3()()=chuancan()=f()+var
# def addd4(a, b):
#     return a + b
# print(addd4(1, 2)(100))
"""----------------------------------装饰类-----------------------------------------"""
def decorator(x):
    def wrapper(*args,**kwargs):
        setattr(x, '属性名', "属性值")
        return x
    return wrapper

@decorator   # demo = decorator(demo)=wrapper
class demo():
    def add(self):
        return "add"
print(demo().__dict__)
"""----------------------------------装饰类的副作用-----------------------------------------"""
def decorator(f):
    def wrapper():
        return f()
    return wrapper
@decorator
def func():
    """这是doc"""
    pass
print(func.__name__, func.__doc__)
# 问题：加了装饰器后，被装饰函数的名字变成wrapper了，doc变成None了，这就是装饰器的副作用
"""----------------------------------装饰类的副作用的消除-----------------------------------------"""
from functools import wraps
def decorator(f):
    @wraps(f)
    def wrapper():
        return f()
    return wrapper
@decorator
def func():
    """这是doc"""
    pass
print(func.__name__, func.__doc__)
"""----------------------------------实战：装饰器实现登录鉴权-----------------------------------------"""
user = {'username':'gaoaolei','password':'1234','isLogin':False}
def login():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == user['username'] and password == user['password']:
        print("登录成功")
        user['isLogin'] = True
    else:
        login()

def decorator(f):
    def wrapper():
        if user['isLogin']:
            return f()
        else:
            login()
            return f()
    return wrapper

@decorator
def get_user_info():
    print(user['username'])

get_user_info()
"""----------------------------------实战：手撕ddt-----------------------------------------"""
# 看另一篇py
# 从例子中可以看到装饰器不一定要是闭包
"""
ddt的原理：
1.利用data装饰器将传入的测试数据保存
2.利用ddt装饰器根据用例条数插入测试用例并绑定对应数据
"""