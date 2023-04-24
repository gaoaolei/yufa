def bibao(x):
    def wrapper():
        print("我是扩展的功能")
        return x()
    return wrapper
@bibao              # @就是调用的意思，等于执行bibao(log)并将返回赋给log，log=bibao(log)=wrapper <==> log()=wrapper()
def log():
    return "hello"
print(log())