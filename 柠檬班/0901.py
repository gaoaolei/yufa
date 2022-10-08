"""1、现有有如下功能函数：
def work(a,b):
    res = a/b
    print('a除B的结果为:',res)
# 调用函数当参数b为0的时候，work执行会报错！如：work(10,0)
# 需求：在不更改函数代码的前提现，实现调用work函数传入参数b为0时，函数不报错，输出结果：参数b不能为零

2、(面试笔试题)请设计一个带参数的装饰器，装饰器接收一个int类型的参数number，可以用来装饰任何的函数，
如果函数运行的时间大于number，则打印出函数名和函数的运行时间"""
import time


def decorator(f):
    def wrapper(a, b):
        if b == 0:
            raise ValueError('b不能为0')
        return f(a, b)

    return wrapper


@decorator
def work(a, b):
    res = a / b
    print('a除b的结果为：', res)


work(10, 4)

start_time = time.time()


def ti(number: int):
    if isinstance(number, int):
        def decorator1(f):
            def wrapper(*args, **kwargs):
                start_time = time.time()
                f(*args,**kwargs)
                end_time = time.time()
                run_time = end_time-start_time
                if round(run_time) > number:
                    return f.__name__, run_time

            return wrapper

        return decorator1
    else:
        raise TypeError('number类型不对')


@ti(1)
def aa():
    time.sleep(2)
print(aa.__name__)


print(aa())
print(aa.__name__)
