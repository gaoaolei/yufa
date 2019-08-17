# _*_coding:utf-8_*_
choose = input('输入s或者p：')
if choose == 's':
    class Student(object):
        # 将方法变成属性
        @property
        def score(self):
            return self._score
        @score.setter
        def score(self,value):
            if (not isinstance(value,int)) or value<0 or value>100:
                raise ValueError('成绩必须为0-100间整数')
            self._score=value
    s=Student()
    s.score=99
    print(s.score)

else:
    class People(object):

        @property
        def birth(self):
            return self._birth

        @birth.setter
        def birth(self, value):
            self._birth = value

        @property
        def age(self):
            return 2017 - self._birth
    p=People()
    p.birth=2011
    print(p.birth)
    print(p.age)
    p.ti=100
    print(p.ti)
