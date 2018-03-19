from django.conf.urls import url

from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^blogArticles.html$',views.arctile),
    url(r'^addArticle.html$',views.addArticle),
    url(r'geTi.html$',views.geTi),
    url(r'test/',views.test),

]