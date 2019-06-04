from django.contrib import admin
from myapp3.models import userinfo

# Register your models here.
class userinfoAdmin(admin.ModelAdmin):  # 数据库字段
    list_display = ['id','name','height']



admin.site.register(userinfo,userinfoAdmin)  # 创建后台管理员用