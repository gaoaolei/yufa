class Animal(object):
    pass
class Mammal(Animal):
    def mam(self):
        print 'is mammal'
class Bird(Animal):
    def bird(self):
        print 'is bird'
class Runnable(Animal):
    def run(self):
        print 'running'
class Flyable(Animal):
    def fly(self):
        print 'flying'
class Dog(Mammal,Runnable,Flyable):
    pass
husky=Dog()
husky.run()
husky.mam()
husky.fly()

