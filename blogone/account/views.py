from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm
from blog.models import BlogArticles

# Create your views here.

def user_login(requset):
    if requset.method == 'POST':
        login_form = LoginForm(requset.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(requset,user)
                # return HttpResponse("Welcome You.You have been authenticated successfully")
                blogs = BlogArticles.objects.all()
                return render(requset,'blog/titles.html', {'blogs': blogs})
            else:
                return HttpResponse("Sorry,Your username or password is not right")

        else:
            return HttpResponse("Invalid login")

    if requset.method == 'GET':
        login_form = LoginForm()
        return render(requset,'account/login.html',{'form':login_form})