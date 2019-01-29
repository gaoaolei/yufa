x = 2
def fun():
    global x
    x = 9
    print(f'local x is {x}')

print(f'global x is {x}')
fun()
print(f'global x is {x}')