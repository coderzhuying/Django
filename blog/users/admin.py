from django.contrib import admin

from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display =  ('name','id','sex','birth')
    list_filter = ['name']



admin.site.register(User,UserAdmin)
