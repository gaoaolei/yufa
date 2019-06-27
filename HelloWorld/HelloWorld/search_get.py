from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from TestModel import models

def search_get(request):
    return render_to_response('search_get.html')

def search_result(request):
    request.encoding = 'utf-8'

    if 'q' in request.GET:
        search_word = request.GET['q']
        if search_word != '':
            models.Test.objects.create(name=search_word)
            # message = '你搜索的内容为：' + search_word
            link = 'https://www.baidu.com/s?ie=UTF-8&wd=%s' % search_word
            return redirect(link)
        else:
            return HttpResponse('你提交了空表单')



