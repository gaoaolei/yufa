# 比较不同
def count():
    list = []
    for i in range(1, 4):
        def f():
             return i*i
        list.append(f)
    return list

for i in count():
    print(i())

# --------------------------------------------

def f(j):
    return j * j
def count():
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs



# 上面的衍生
def f(j):
    def g(k):
        return j * j + k
    return g
def count():
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

list = count()
print(list[1](2))


