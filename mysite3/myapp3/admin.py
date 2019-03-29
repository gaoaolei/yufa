from django.contrib import admin
from myapp3.models import userinfo

# Register your models here.
class userinfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','height']



admin.site.register(userinfo,userinfoAdmin)