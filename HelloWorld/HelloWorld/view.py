from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

def hello(request):
    # return HttpResponse('hello world!')
    return render(request, 'hello.html', {"hello":'hello, i love u!!!'})
