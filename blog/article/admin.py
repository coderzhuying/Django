#coding=utf-8
from django.contrib import admin

from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display =  ('title','id','content')
    list_filter = ['title']



admin.site.register(Article,ArticleAdmin)