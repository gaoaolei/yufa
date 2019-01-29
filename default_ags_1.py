def add_end(L=None):
    if L is  None:
        L=[]

    L.append('END')
    return L
m=[1,2,3,4]
print add_end()
print add_end()
print add_end(m)
print add_end(m)
print add_end(m)