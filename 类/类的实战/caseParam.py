# 用例参数以excel形式存储
# 为什么要设计这么一个类？
# 答：因为如果不设计，Excel的数据读出来就是list形式，取值的时候就需计算index，且字段顺序变化会导致维护很麻烦，所以需要加这么一个类。类似结构体


class CaseParam(object):
    def __init__(self):
        self.order = None
        self.app_version = None
        self.channel = None
        self.all_param = dir(self)
