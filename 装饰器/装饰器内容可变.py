def endsign(var):
    def decorator(func):
        def wrapper():
            return func() + var
        return wrapper
    return decorator
@endsign('!!')
# 等效于执行了hello = endsign('!!')(hello) = decorator(hello) = wrapper
def hello():
    return 'hello'
@endsign('??')
def hi():
    return 'hi'
print(hello())
print(hi())
