# 递归函数其实很简单，只要找到递归的终点就行了
# n! = n*(n-1)*(n-2)...*1 = n*(n-1)!
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

# sum(n) = n+(n-1)+(n-2)+...+1 = n+sum(n-1)
def sum(n):
    if n == 1:
        return 1
    return n+sum(n-1)
print(sum(100))


def fact_iter(num, product):
    if num == 1:
        return  product
    return fact_iter(num - 1, num * product)

print(fact_iter(5,3))

