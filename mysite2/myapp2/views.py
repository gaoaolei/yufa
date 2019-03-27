from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp2.models import UserWeight

def caozuo(request):
    UserWeight(name='gaoaolei',weight='60').save()
    UserWeight.objects.create(name='daiqiaozhen',weight=48)    # 等价上一句话

    temp = UserWeight.objects.filter(id=13)    #列表
    # print(type(temp))
    # for item in temp:
    #     print(item.id,item.name,item.weight)
    #
    # temp1 = UserWeight.objects.get(id=13)  # 字典
    # print(type(temp1))
    # temp1.name='gaoleqi'
    # temp1.save()
    temp.update(name='gaoerzi')
    # print(temp1.id, temp1.name, temp1.weight)

    return HttpResponse('save successful!')

# models.UserInfo.objects.create(username=username1,password=password1)
# test=models.UserInfo(username=username1,password=password1)
# test.save()

