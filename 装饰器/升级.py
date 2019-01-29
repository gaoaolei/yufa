def endsign(var):
    def decorator(func):
        def wrapper(*c, **d):
            return func(*c, **d) + var
        return wrapper
    return decorator

@endsign('!!')
def hello(a, b):
    return 'hello, %s %s' % (a, b)

@endsign('戴巧珍')
def hi():
    return 'hi'

print(hello('gao', 'ao'))
print(hi())

