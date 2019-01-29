def endsign(func):
    def wrapper(*args, **keyword):
        return func(*args, **keyword) + '!!'
    return wrapper
@endsign
def hello(args1, args2):
    return 'hello %s %s' % (args1, args2)
a = 'gaopeng'
b = 'gaoaolei'
print(hello(a, b))


