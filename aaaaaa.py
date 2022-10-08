class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def __call__(self, *args, **kwargs):
        return self


print(callable(Person))

import inspect

print(inspect.getmembers(Person))
print(Person.__dict__)
p = Person('gaoaolei', '30')
print(callable(p))
print(inspect.getmembers(p))
print(inspect.getmembers(p, lambda x: isinstance(x, str)))
print(inspect.getmodulename("./kube/kube.py"))
print(inspect.ismodule('0830'))
print(__file__)
print(__name__)
# import pandas
# pandas.DataFrame
from inspect import signature


def foo(a, b, *, c: int, **kwargs) -> list[int]:
    pass


sign = signature(foo)
print(repr(sign))
print(sign.parameters['c'])
print(sign.parameters['c'].annotation)
print(sign.return_annotation)

import pprint

data = [1, 2, 3, 4,
        5]
print(data)
print("--------分界线--------------")
pprint.pprint(data)


def demo(a, b):
    """nihao"""
    pass


print(demo.__name__)
print(demo.__doc__)
from functools import partial

d = partial(demo, b=1)
# print(d.__name__)
# print(d.__doc__)

from functools import update_wrapper, wraps


def wrap2(func):
    @wraps(func)
    def inner(*args):
        return func(*args)

    return inner


@wrap2
def demo():
    print('hello world')

print(demo.__name__)

import time
start_time = time.time()
from functools import lru_cache
@lru_cache(maxsize=30)  # maxsize参数告诉lru_cache缓存最近多少个返回值
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print([fib(n) for n in range(33)])
fib.cache_clear()   # 清空缓存
end_time=time.time()
print(end_time-start_time)

"eyJhdmF0YXIiOiJodHRwczovL3dwaW1nLndhbGxzdGNuLmNvbS9mNzc4NzM4Yy1lNGY4LTQ4NzAtYjYzNC01NjcwM2I0YWNhZmUuZ2lmIiwidXNlcm5hbWUiOiJnYW9hb2xlaUAxOXBheS5jb20uY24iLCJuYW1lIjoiXHU5YWQ4XHU1MGIyXHU5NmY3IiwidXNlcl9pZCI6IjY4OTEyOTQ0MDU1MDMyNjI3MiJ9:1oU2t0:M3Kvf8a0PPYEQiJS1Q4ONtJi9VT_x0ZjOcftHpNAVKs"