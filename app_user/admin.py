from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from app_user.models import Publisher


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('StudentName', 'CardID', 'UID') #根据属性搜索
    list_display = ('StudentName', 'CardID', 'UID')   #列表显示的属性
    list_filter = ('StudentName',)                        #筛选
    pass
admin.site.register(Publisher,PublisherAdmin)
