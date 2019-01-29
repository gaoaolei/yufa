L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def order_by_name(n):
    return L[n][0]
print sorted(L,key=order_by_name)