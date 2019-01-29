valary=[('gaoaolei',1000),('gaorui',18)]
fs='''%-10s valary:%5f$
%-10s valary:%5s$'''
print(fs   %(valary[0][0],valary[0][1],valary[1][0],valary[1][1]))

print('%x' %108)
print('%X' %109)
print('%#x' %108)
print('%#X' %109)
print('%f' %123)
print('%.2f' %123.678889)
print('%19.3f' %123.45678)
print('%019.3f' %123.45678)

# ?????
printv('my name is {}'.format('gaoaolei'))
print ('my name is {1},{0} years old'.format(28,'gaoaolei'))#????
print ('my name is {a},{b} years old'.format(b=28,a='gaoaolei'))#????
print('{}'.format(56))
print('{:10}'.format(56))
print('{:<10}'.format(56))# ???
print('{:010}'.format(56))
print('{:x}'.format(56))
print('{}??{{??}}'.format(110))  #????????
print('??')

# python3.6????
name='gaoaolei'
print(f'my name is {name} ')
print('my name is ',name)

# ???
print('my name is \'gaooalei\'')
print('\x41')

#???????
a=input('please input your name:')
print(a)
age=input('input your age:')
if int(age)>25:
    print ('nilaole')
else:
    print ('lianqing')

