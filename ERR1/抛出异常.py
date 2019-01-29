class FooError(ValueError):     # 可以不用尽量不用
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

foo('0')