from django.shortcuts import render
from myapp import models

# Create your views here.
from django.shortcuts import HttpResponse

def index(request):
    # return HttpResponse('Hello World!')
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username1 = request.POST.get('username', None)
        password1 = request.POST.get('password', None)
        weight1 = request.POST.get('weight',None)
        # print(username, password)
        # return render(request,'index2.html')
        # user_list.append({'username': username, 'password': password})
        models.UserInfo.objects.create(username=username1,password=password1)
        models.UserData.objects.create(weight=weight1)
        print(models.UserData.objects.all())

    user_list = models.UserInfo.objects.all()
    print(user_list)

    return render(request, 'login.html', {'data': user_list})


