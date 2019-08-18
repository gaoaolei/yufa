#! /user/bin/env python
stack=[]
def pushit():
      stack.append(input("enter your string: ").strip())
def popit():
      if len(stack)==0:
            print("the stack is empty")
      else:
          #  stack.pop()
            print("Remove",stack.pop(),"secuss!")
def viewstack():
      print(stack)
CMDs={'u':pushit,'o':popit,'v':viewstack}
def showmenu():
      pr='''
      p(U)sh
      p(O)p
      (V)iew
      (Q)uit
      Enter choice:'''
      while True:
            while True:
                  try:
                        choice=input(pr).strip()[0].lower()
                  except (EOFError,KeyboardInterrupt,IndexError):
                        choice='q'
                  print("you picked: %s" % choice)
                  if choice not in "uvop":
                        print('Invalid option,try again')
                  else:
                        break
            if choice=="q":
                  break
            CMDs[choice]()
if __name__=='__main__':
      showmenu()
      
      
