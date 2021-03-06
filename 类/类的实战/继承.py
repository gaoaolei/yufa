# 类的继承，子类先到自己中查找方法（含__init__(属性)方法和普通方法），没有就去父类中找
# 如果想在不完全重写的情况下给子类增加属性，需要在子类的方法中显示的调用父类的方法  super(子类, self).__init__(*args)

class A(object):
    def __init__(self, name):
        self.name = name
        # print(self.name)

    def getName(self):
        print("A 方法")


class B(A):
    def __init__(self, name, age):
        super(B, self).__init__(name)
        # self.name = name
        self.age = age
        # print(self.name)

    def getName(self):
        super(B, self).getName()
        return self.name, self.age


if __name__ == "__main__":
    b = B("gaoaolei", 10)
    print(b.getName())
