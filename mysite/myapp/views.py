from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
def index(request):
    # return HttpResponse('Hello World!')
    if request.method == 'POST':
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        print(username,password)
        return render(request,'index2.html')
    return render(request, 'index.html',)



