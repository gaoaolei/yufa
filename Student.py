class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    def print_score(self):
        print ('%s:%s' %(self.name,self.score))
a=Student('gaoaolei',23)
print a.name
print a.score
print a.get_grade()
a.print_score()
print '----------------------------------------------------'
class Animal(object):
    def run(self):
        print 'animal is running'
class Dog(Animal):
    def run(self):
        print 'dog is running'
class Cat(Animal):
    def run(self):
        print 'cat in running'
class Tortoise(Animal):
    def run(self):
        print 'tortoise runs slowly'
def run_twice(a):
    a.run()
    a.run()
a=Animal()
a.run()
b=Dog()
b.run()
c=Cat()
c.run()
run_twice(a)
run_twice(b)
run_twice(c)
run_twice(Tortoise())






