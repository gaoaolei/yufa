from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def hello_world(request):
    return HttpResponse('hello world')

def article_content(request):
    art = Article.objects.all()[0]

    title = art.title
    brief_content = art.brief_content
    content = art.content
    article_id = art.article_id
    publish_time = art.publish_time

    return_str = 'title:%s,brief_content:%s,content：%s,article_id:%s,publish_time:%s' %(title,brief_content,content,article_id,publish_time)

    return HttpResponse(return_str)