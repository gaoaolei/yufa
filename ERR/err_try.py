# _*_ coding:utf-8 _*_
a = range(100)
a[11]

try:
    print('trying')
    a = range(100)
    a[11]
except LookupError as o:
    print ('except:', o)
finally:
    print('我被执行了')
print('我是主函数')

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')





