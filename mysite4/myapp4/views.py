from django.shortcuts import HttpResponse, render, redirect

# Create your views here.
def index(request):
    # return HttpResponse('hello world')
    # return render(request, 'index.html')
    return redirect('https://www.baidu.com')
