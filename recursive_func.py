def recursive_func(x):
    if x==1:
        return 1
    print('a')
    return recursive_func(x-1)*x
print(recursive_func(5))

