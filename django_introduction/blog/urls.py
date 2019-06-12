from django.urls import path, include
from blog.views import hello_world, article_content

urlpatterns = [
    path('hello_world/', hello_world),
    path('article_content/', article_content)
]