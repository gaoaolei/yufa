class A():
    def __init__(self,a,b):
        self.x=''
        self.y=''
        if a+b == 3:
            self.x = 1
            self.y = 'abc'

A = A(2,1)
print(A.y)