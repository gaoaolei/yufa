# !/usr/bin/env/ python
# _*_coding:utf-8_*_
class Student(object):
    pass
def set_score(self,score):
    self.score=score
from types import MethodType
# Student.set_score=MethodType(set_score, None, Student)    # 直接对所有实例绑定外部方法==直接定义类的内部方法
s1=Student()
s2=Student()
s1.set_score=MethodType(set_score, s1, Student)         # MethodType给实例s1创建了指向外部函数set_socre的链接
s2.set_score=MethodType(set_score, s2, Student)
s1.name='gaoaolei'
print s1.name
s2.name='daiqiaozhen'
print s2.name
s1.set_score(100)
s2.set_score(50)
print s1.score
print s2.score