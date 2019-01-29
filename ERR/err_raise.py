class V(ValueError):
    pass
def f(s):
    print('s!=0')
    if s == 0:
        raise V('zhe ge zhi cuo wu le ')
f(0)