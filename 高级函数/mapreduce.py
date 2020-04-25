# _*_coding:utf-8_*_
def f(x):
    return x*x
print map(f, (1,2,3,4,5,6,7,8))

def add(x,y,a):
     return a(x)+a(y)
print add(-5,5,abs)
print map(str,[1,2,3,4,56,])

from functools import reduce                # 为什么有没有这一句都一样
def gao(x,y):
    return x*10+y
print reduce(gao,[1,2,3,4,5])

def append(x,y):
    return x+y
print reduce(append,[1,2,3,4,5])






