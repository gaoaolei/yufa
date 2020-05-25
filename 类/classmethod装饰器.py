class DemoClass:

       @classmethod

       def classPrint(self):

              print("class method")

       def objPrint(self):

              print("obj method")

 

obj = DemoClass()

obj.objPrint()

obj.classPrint()

 

DemoClass.classPrint()

