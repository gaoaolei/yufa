import random

list = []
for i in range(0,6):
    if i == 2 or i == 4:
        a = random.randrange(0,9)
        b = str(a)
        list.append(b)
    else:
        a= random.randrange(65,91)
        b = chr(a)
        list.append(b)
res = ''.join(list)
print(res)
