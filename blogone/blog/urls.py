from django.conf.urls import url
from .import views
import blog

urlpatterns=[
    url(r'^$',views.blog_title,name='blog_title'),
    url(r'(.+)$',views.blog_article,name="blog_detail")
]
handler404 = blog.views.page_not_found