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




