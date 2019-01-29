# _*_coding:utf-8_*_
print sorted((1,2,-10,9,0,-2838238))
print sorted([1,2,-10,9,0,-2838238])
print sorted([1,2,-10,9,0,-2838238],key=abs)
print sorted(['bob', 'about', 'Zoo', 'Credit'])
print sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 可以实现，但不知道意义
def order_by_name(x):
    list=[]
    n=0
    while n<4:
        list.append(x[1])
        n=n+1
    print list
print sorted(L,key=order_by_name)
# 自定义函数实现
def order_by_name1(x) :
    return x[0]
print sorted(L, key=order_by_name1)
# 内置函数实现
from operator import itemgetter
print sorted(L,key=itemgetter(1))

