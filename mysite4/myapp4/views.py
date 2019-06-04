from django.shortcuts import HttpResponse, render, redirect

# Create your views here.
def welcome(request):
    # return HttpResponse('hello world')
    return render(request, 'welcome.html')
    # return redirect('https://www.baidu.com')

def index(request):
    return render(request, 'index.html')