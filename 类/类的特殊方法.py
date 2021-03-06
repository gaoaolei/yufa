import math


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __float__(self):
        return math.hypot(self.x, self.y)  # 平方根函数

    def __mul__(self, beishu):
        x = self.x * beishu
        y = self.y * beishu
        return Vector(x, y)

    def __str__(self):
        return 'Vector(%s,%s)' % (self.x, self.y)

    mo = __float__  # 因为hypot返回的是float型，所有必须是特殊方法__float__或者__abs__（目前我已知的），但是这样就不直观，所以有这句话


v1 = Vector(2, 3)
v2 = Vector(4, 4)
v3 = v1.__add__(v2)
v4 = v1 + v2
print(v3, v4)
print(v3.mo(), v3.__float__(), float(v3))
