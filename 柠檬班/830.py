"""
1、现在有一个列表   li = [11,21,4,55,6,67,123,54,66,9,90,56,34,22],
请将 大于5的数据过滤出来，然后除以2取余数，结果放到一个生成器中

2、定义一个可以使用send传入域名，自动生成一个在前面加上http://，在后面加上路径/user/login的url地址，

生成器最多可以生成5个url,生成5条数据之后再去生成，则报错StopIteration

使用案例：

# 例如:
res = g.send('www.baidu.com')
# 生成数据res为：http://www.baidu.com/user/logim'

3、面试笔试扩展题
有一个正整数列表(数据是无序的,并且允许有相等的整数存在),
编写一个能实现下列功能的函数，传入列表array,和正整数X，返回下面要求的2个数据
def func(array, x)
    '''逻辑代码'''
    return count, li
1、统计并返回在列表中,比正整数x大的数有几个(相同的数只计算一次)，并返回-----返回值中的的count
2、计算列表中比正整数X小的所有偶数，并返回  -----------返回值中的li
"""
li = [11, 21, 4, 55, 6, 67, 123, 54, 66, 9, 90, 56, 34, 22]
res1 = map(lambda x: x % 2, filter(lambda x: x > 5, li))
print(list(res1))


print('------------------第二题-----------------')
def deal_url():
    for i in range(5):
        res = yield
        print('http://' + res + '/user/login')


d = deal_url()
d.send(None)
d.send('www.baidu.com')
d.send('www.lemon.com')
d.send('www.lemon1.com')
d.send('www.lemon2.com')
# d.send('www.lemon3.com')



print('------------------第三题------------------')
l = [6, 3, 5, 7, 3, 5, 6, 8, 4, 1, 0, 5, 9, 22, 22, 2, 2, 2, 2, 2]

def fun(array, x):
    count = len(set(filter(lambda i: i > x, array)))
    li = list(filter(lambda j: j < x and j % 2 == 0, array))
    return count, li


print(fun(l, 3))
