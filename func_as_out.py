# _*_coding:utf-8_*_
def lazy_sum(*args):           # 参数在外部函数中
    def sum():                 # 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
                               # 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
        s = 0
        for x in args:
            s = s + x
        return s
    return sum
f1=lazy_sum(1,2,3,4)
f2=lazy_sum(1,2,3,4)
f3=lazy_sum(1,2,3,5)
f4=lazy_sum(1,2,3,5)
f5=lazy_sum(1,2,3,5)
print f1==f2
print f1==f3
print f1()==f2()
print f1()==f3()
print f1,f2,f3,f4,f5,lazy_sum
print f1(),f2(),f3()
print lazy_sum




