"""
1.data保存测试数据
2.ddt根据测试数据生成测试
3.用例传入数据，使用闭包实现
4.数据是动态的，需要锁定，通过闭包锁定
"""
# from ddt import ddt, data
import unittest


def add(x, y):
    """被测函数"""
    return x + y


def data(*args):
    def wrapper(func):
        setattr(func, 'datas', args)
        return func

    return wrapper


def add_case(params, method):
    def wrapper(self):
        method(self, params)

    return wrapper


def ddt(cls):    # ddt是装饰器，但不是闭包
    print(list(cls.__dict__))
    for name, method in list(cls.__dict__.items()):
        if hasattr(method, 'datas'):
            datas = getattr(method, 'datas')
            for index, data in enumerate(datas):
                method_name = "{}_{}".format(name, index)

                setattr(cls, method_name, add_case(data, method))
            delattr(cls, name)
    print(cls.__dict__)
    return cls


"""测试数据"""
test_datas = [(1, 2, 3), (2, 3, 5), (-3, 4, 1), (0, 2, 2), (100, 10000, 10100)]


@ddt
class TestClass(unittest.TestCase):

    @data(*test_datas)  # @data(test_datas)=@wrapper -----test_add = wrapper(test_add)=test_add
    def test_add(self, item):
        assert add(item[0], item[1]) == item[2]


if __name__ == "__main__":
    import unittestreport

    suite = unittest.defaultTestLoader.discover(r'/')
    unittestreport.TestRunner(suite).run()
