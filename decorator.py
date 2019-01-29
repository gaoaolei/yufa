# _*_coding:utf-8_*_
'''def example():
    print "gaoaolei zhen shuai!"
b=example
b()

print b.__name__
print example._name_
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print ('gaoaolei')
now()
@log
def nihao():
    print 'nihao'
nihao()
