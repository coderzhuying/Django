from django.conf.urls import url

from . import views
urlpatterns=[
    url(r'^$',views.gerenyemian),
    url(r'^xiangCe.html$',views.xiangCe),
    url(r'^gerenyemian.html$',views.gerenyemian),
    url(r'^uploadPic.html$',views.uploadPic),
    url(r'^uploadHandle.html$',views.uploadHandle),
    url(r'^register.html$',views.register),
    url(r'^signin.html$',views.signin),
    url(r'^registerHandle$',views.registerHandle),
    url(r'^signinHandle$',views.signinHandle),
    url(r'^infoHandle$',views.infoHandle)
]
