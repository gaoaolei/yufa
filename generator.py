print(list(range(10)))

print([x*x for x in range(1,11)])

print([m+n for m in 'ABC' for n in 'XYZ'])
for m in 'abc':
    for j in 'def':
        for k in 'hij':
            print(m+j+k)


print([x * x for x in range(1, 11) if x % 2 == 0])
print([x * x for x in range(1, 11)[1::2]])

import os
print([d for d in os.listdir('.')])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

g=(x*x for x in range(10))
# print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())
# print(next(g))


