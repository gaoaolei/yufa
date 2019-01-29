def f(j):
    def g(k):
        return j * j + k
    return g
def count():
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
(a, b, c) = count()
print (c(1))

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
(a, b, c) = count()
print (c())


def f(j):
    def g(k):
        return j * j + k
    return g
def count():
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
print (count()[2](3))
