# _*_coding:utf-8_*_
class Student(object):
    def get_score(self):
        return self.score
    def set_score(self,value):
        if (not isinstance(value,int)) or value<0 or value>100:
            raise ValueError('成绩必须为0-100间整数')
        self.score = value
s=Student()
a=99
s.set_score(a)
print s.get_score()

