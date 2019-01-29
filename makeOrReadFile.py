#!/user/bin/env python
s=raw_input("if u want to make file ,please enter make;if u want to read file,please enter read\n>> ")
if s=="make":
      #!/user/bin/env python
      import os
      ls=os.linesep
      fname=raw_input("enter filename>")
      print fname
      while True:
            if os.path.exists(fname):
                  print 'error:"%s" already exist' % fname
            else:
                  break

      all=[]
      print "enter lines('.' by itself to quit)."

      while True:
            entry=raw_input(">")
            if entry==".":
                  break
            else:
                  all.append(entry)

      fobj=open(fname,"w")
      fobj.writelines("%s%ls" % (x,ls) for x in all)
      fobj.close()
      print "DONE"
if s=="read":
      fname=raw_input("name of file you want to open:")
      fobj=open(fname,"r")
      for i in fobj:
            print i,
      fobj.close()
