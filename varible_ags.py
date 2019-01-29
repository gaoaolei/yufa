def sqr_sum(*nums):
    sum=0
    for n in nums:
        sum+=n*n
    return sum
l=[1,2,3,4]
print sqr_sum(*l)