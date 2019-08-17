def sort1(x):
    for j in range(0, len(x)-1):        # 要比较len()-1次
        for i in range(0, len(x)-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    return x
list = [13, 22, 4, 60, 8]
print(sort1(list))

g = [x[i] for j in range(len(x)-1) for i in range(len(x)-1) if x[i]>x[i+1]:(x[i], x[i+1] = x[i+1], x[i])]

# 优化之后
def sort2(x):
    for j in range(len(x)-1, 0, -1):
        for i in range(0, j):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    return x
l = [23, 12, 8, 6, 4]
print(sort2(l))

def sort3(x):
    a = []
    for i in range(len(x)):
        a.append(min(x))
        x.remove(min(x))
    return a
y = [5, 3, 4, 9, 19, 2, 1, 3]
print(sort3(y))





