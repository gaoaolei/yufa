# _*_coding:utf-8_*_
print(list(map(lambda x:x*x,[1,2,3,4,5])))

f=lambda x : x * x
print(f)
print(f(5))

def build(x, y):
    return lambda: x*x + y*y        # 匿名函数作为返回值，lambda的参数取自外部函数，所以这里没有
f = build(1,3)
print(f())

