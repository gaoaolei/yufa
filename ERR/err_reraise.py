def bar(s):
    try:
        10/s
    except ValueError as e:
        print('ValueError!')
        raise ValueError('inv alid value: %s' % s)
bar(0)
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#
# bar()