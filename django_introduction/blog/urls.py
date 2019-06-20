from django.urls import path, include
from blog.views import hello_world, article_content, get_index_page,get_detail_page

urlpatterns = [
    path('hello_world/', hello_world),
    path('article_content/', article_content),
    path('index/', get_index_page),
    # path('detail', get_detail_page),
    path('detail/<int:middle_article_id>', get_detail_page),  # 将middle_article_id传递给get_detail_page()
]