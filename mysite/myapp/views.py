from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def index(request):
    # return HttpResponse('Hello World!')
    return render(request, 'index.html')

def login(request):
    user_list = []
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username, password)
        # return render(request,'index2.html')
        user_list.append({'username': username, 'password': password})
        print(user_list)

    return render(request, '.html', {'data': user_list})



