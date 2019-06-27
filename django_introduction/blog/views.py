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

def get_index_page(request):
    all_article = Article.objects.all()
    new_article = Article.objects.order_by('-publish_time')[0:2]
    return render(request, 'index.html', {'article_list':all_article,'new_article':new_article})

def get_detail_page(request, middle_article_id):
    articles = Article.objects.all()
    for i in range(0,len(articles)):
        if articles[i].article_id == middle_article_id:
            if i == 0:
                previous_article = articles[i]
                next_article = articles[i+1]
            elif i == len(articles)-1:
                previous_article = articles[i-1]
                next_article = articles[i]
            else :
                previous_article = articles[i-1]
                next_article = articles[i+1]
        else:
            continue


    # 简单方法
    curr_article = Article.objects.get(article_id=middle_article_id)

    # 笨方法
    # articles = Article.objects.all()
    # curr_article = None
    # for article in articles:
    #     if article.article_id == middle_article_id:
    #         curr_article = article
    #         break
    section_list = curr_article.content.split('\n')   # 为了换行，好看点
    return render(request, 'detail.html', {'curr_article':curr_article,
                                           "section_list":section_list,
                                           'next_article':next_article,
                                           'previous_article':previous_article})