def func(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

args = (1, 2, 3, 4, 5)
kw = {'x': 99}
func(*args, **kw)

#daf asdf