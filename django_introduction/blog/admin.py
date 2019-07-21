from django.contrib import admin
from  blog import models
# Register your models here.
# admin.site.register(models.Article)
class A(admin.ModelAdmin):
    list_display = ('article_id','title','brief_content','content','publish_time')
    list_filter = ('title',)
    list_per_page = 3
    ordering = ('article_id',)
    search_fields = ('title',)

    #自定义表单（add页面）
    fields = ('title', 'brief_content')
admin.site.register(models.Article, A)