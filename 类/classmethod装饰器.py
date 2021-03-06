# 类  ：可以查询/修改类属性，可以调用类方法
# 实例：可以查询/修改实例属性，可以调用实例方法；实例属性实例方法不存在时，会查询但不能修改类属性，会调用类方法。
class A(object):
    age = 31  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性

    @classmethod
    def class_print(afds):  # 类方法
        print("class method")

    def class_print(self):  # 实例方法
        print("obj method")


A.age = 40
A(20).age=21
A(20).class_print()
print(A.age)
print(A(20).age)
