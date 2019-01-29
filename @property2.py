# _*_coding:utf-8_*_
class Student(object):
    @property
    def score(self):
        return self.score
    @score.setter
    def score(self,value):
        if (not isinstance(value,int)) or value<0 or value>100:
            raise ValueError('成绩必须为0-100间整数')
        self.score=value
s=Student()
s.core=99
print s.core

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
print p._birth
print p.age
p.time=100
print p.time
