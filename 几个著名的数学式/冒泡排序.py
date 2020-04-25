# 内建sorted()
y = [5, 3, 4, 9, 19, 2, 1, 3]
print(sorted(y))


def sort1(x):
    '''冒泡排序'''
    for j in range(0, len(x)-1):        # 要比较len()-1次
        for i in range(0, len(x)-1):
            if x[i] > x[i+1]:   # 降序排列只需改成小于号
                x[i], x[i+1] = x[i+1], x[i]
    return x
list = [13, 22, 4, 60, 8]
print(sort1(list))

def sort2(x):
    a = []
    for i in range(len(x)):
        a.append(min(x))  # 降序用max
        x.remove(min(x))
    return a
y = [5, 3, 4, 9, 19, 2, 1, 3]
print(sorted(y))
print(sort2(y))





