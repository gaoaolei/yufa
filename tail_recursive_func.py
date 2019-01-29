def fact_iter(num, product):
    if num == 1:
        return  product
    return fact_iter(num - 1, num * product)

print fact_iter(5,1)
