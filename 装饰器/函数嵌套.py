def endsign(func):
    def wrapper():
        return func() + '!!'
    return wrapper
@endsign
# 等同于执行了hello=endsign(hello)
def hello():
    return 'hello'
@endsign
def hi():
    return 'hi'

print(hello())
print(hi())





# 带参数（装饰器内函数参数形式和被装饰函数参数形式一致就行），可以固定写*args，**keyword，包含所有参数形式
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






