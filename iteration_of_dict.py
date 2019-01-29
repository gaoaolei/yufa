d={1:'x',2:'y',3:'z'}
for ke in d.keys():
    print ke
for val in d.values():
    print val
for k,v in d.items():
    print k,v

from collections import Iterable
print isinstance((1,2,3),Iterable)