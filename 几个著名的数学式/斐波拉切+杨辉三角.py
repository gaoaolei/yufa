# 1, 1, 2, 3, 5, 8, 13, 21, 34, ..
def fib(max):
    a = [1, 1]
    for i in range(2, 100):
        x = a[i - 1] + a[i - 2]
        if x >= max:
            break
        a.append(x)
    print(a)


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b  # 注意不能分开写，注意区别，这种赋值，先计算等值右边就是b=1 a+b=1再赋值给a和b，那么 a=1, b=1
        n = n + 1
    return 0


def fib3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b  # 注意不能分开写，注意区别，这种赋值，先计算等值右边就是b=1 a+b=1再赋值给a和b，那么 a=1, b=1
        n = n + 1
    return 0


fib2(10)


class Fib():
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):     # 可以index取值
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


fib4 = Fib()
for i in fib4:
    print(i)
print(fib4[5])


# 杨辉三角
def yanghui():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]


j = 0

for i in yanghui():
    print(i)
    if j > 10:
        break
    j = j + 1
