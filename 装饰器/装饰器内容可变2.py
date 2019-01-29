def endsign(func):
    def wraper():
        def tail(var):
            return func() + var
        return tail
    return wraper
@endsign
def hello():
  return 'hello world'
@endsign
def hi():
    return 'hi world'

print(hello()('!!'))
print(hello()('??'))
print(hi()('!!'))
print(hi()('??'))