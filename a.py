f = open('content','r')
content = f.readlines()
print(content)

l = [i.strip('\n').split(',') for i in content]
print(l)
l1=list()
for i in l[1:]:
    d = dict()
    for j in list(zip(l[0],i)):
        d.update({j[0]:j[1]})
    l1.append(d)
print(l1)
