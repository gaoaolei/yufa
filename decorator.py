def log(func):
    def wrapper(*args, **kw):
        print('我是装饰用的小花朵，调用我的都有花朵装饰哦')
        return func(*args, **kw)
    return wrapper
# 上面的装饰函数固定抄写套用就行了，不用修改，除了print

@log
def a(x,y=2):
    return pow(x,y)

@log
def b(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

if __name__ == '__main__':
    print(a(2,3))
    print(b(*list(range(101))))

