class Animal(object):
    def run(self):
        return  'animal is running'
    def run1(self):
        return 'animal1 is running'

class Dog(Animal):
    def run(self):
        print 'dog in running'
class Cat(Animal):
    def run(self):
        print 'cat in running'

    def run_twice(self):
        return self.run(), self.run()
# def run_twice(a):
#     a.run()
#     a.run()
a=Animal()
b=Dog()
c=Cat()
print a.run_twice()
print a.run1()
print b.run_twice()


