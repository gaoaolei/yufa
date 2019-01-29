#!/user/bin/env python
import string
a=raw_input("enter string need check:")
if len(a)>1:
      if a[0] not in string.letters+"_":
            print "the string must be start with alpha or _ "
      else:
            for otherChar in a[1:]:
                  if otherChar not in string.letters+string.digits:
                        print "not is string"
                        break
            else :      
                  print "is string"
