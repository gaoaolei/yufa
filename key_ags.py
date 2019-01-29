def person(name, age,**keyword):
    print 'name',name,  'age',age,   'other',keyword

person('gaoaolei',28)
person('gaoaolei', 28, shengao = 178, city = 'shanghai')

keyword = {'shengao':178, 'city':'shanghai'}
person('gaoaolei', 28, shengao=keyword['shengao'], city=keyword['city'])
person('gaooalei', 28, **keyword)