L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return sorted(t, key = lambda x : x[1])
print(by_name(L))

'''
1.sort()
list的方法，只做修改，不返回值，list.sort(),
2.sorted()
序列的方法，返回新值，list2=sorted(list1,key=..)

1.默认排序：第一个值比较，再第二个值比较，依次。。  sort()
2.自定义排序：key=list[x],按指定的第几个元素排列
    a.用匿名函数
    sort(key=lambda x:x[2])
    b.也可以定义函数
    def a(ele):
        return ele[2]
    list.sort(key=a)

1.sort(reverse=True)倒序排列

1.多次排序：多次使用sort或sorted
2.多阶排序：
    a.定义多个key
    sort(key=lambda x:(x[1],x[2])表示先按第2个元素排序，再按第3个元素排序
    def a(ele):
        return ele[1],ele[2]
    list.sort(key=a)
    b.使用模块operator
    import operator
    a = [(1, 2, 3), (3, 4, 5), (0, 1, 2)]
    a.sort(key=operator.itemgetter(1, 2))
    c.多阶排序的倒序问题
    如果多个key并都是顺序或者倒序，则需要再key的返回值之前加负号，但必须是int型，字符型目前不知道怎么处理！！！
    sort(key=lambda x:(x[1],-x[2])表示先按第2个元素顺序，再按第3个元素倒序（若有reverse=True，则反过来）
    return ele[1],-ele[2]
'''
