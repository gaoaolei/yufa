print(dict(a='ad',b=2))
print(dict([('1',2),('a',3)]))
print(dict(zip(['a','b'],[1,2])))


print(["data{}".format(i) for i in range(100) if i % 2 == 0])

print([f"data{i}" for i in range(100) if i % 2 == 0])

print([f"data{i}" if i % 2 == 0 else f"lemon{i}" for i in range(100)])
a = ([f"data{i}" if i % 2 == 0 else f"lemon{i}" for i in range(100)])

li = ['gao', 'ao', 'lei']
print({k: v for k, v in enumerate(li)})
print({i[0]: i[1] for i in enumerate(li)})
print({k: v for k, v in enumerate(li) if k > 0})
# print({k: v.upper() if v.startswith('a') else k: v for k, v in enumerate(li)})  不支持三目？

# 列表推导式
dic = {'a': 1, 'b': 2, 'c': 3}
res = [(k, v) for k, v in dic.items()]
print(res)
# [('a',1),('b',2),('c',3)]

res = ((k, v) for k, v in dic.items())
print(list(res))
print(tuple(res))  # 结果为空，因为上一条已经将值取走了  

'''
Iterable()      可迭代对象
Iterator()      迭代器，继承自Iterable
Generator()     生成器，继承自Iterator
'''
from collections.abc import Iterable,Iterator,Generator

a,b = {1,2}
print(a,b)
name = "Fred"
print(f"He said his name is {repr(name)}")