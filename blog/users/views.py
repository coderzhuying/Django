from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse,JsonResponse
import os
from django.conf import settings
from django.contrib import messages
import json
# Create your views here.

def gerenyemian(request):

    uname = request.session['uname']
    sex = request.session['sex']
    work = request.session['work']
    birth = request.session['birth']
    ad = request.session['ad']
    desc = request.session['desc']

    context = {'uname':uname,'sex':sex,'work':work,'birth':birth,'ad':ad,'desc':desc}


    return render(request,'users/gerenyemian.html',context)

def xiangCe(request):

    return render(request,'users/xiangCe.html')

def uploadPic(request):

    return render(request,'users/uploadPic.html')

def uploadHandle(request):

    pic1 = request.FILES['pic1']

    picName = os.path.join(settings.MEDIA_ROOT,pic1.name)

    with open(picName,'wb+') as pic:

        for c in pic1.chunks():

            pic.write(c)

    path = "/static/media/"+pic1.name

    listp = [path]

    context = {list:listp}

    return render(request,'users/uploadHandle.html',context)
#<img src="/static/media/%s"/ >%pic1.name


def register(request):

    return render(request,'users/register.html')

def signin(request):

    return render(request,"users/signin.html")

def registerHandle(request):

    post = request.POST

    uname = post.get('user_name')

    upwd = post.get('pwd')

    cpwd = post.get('cpwd')

    count = User.objects.filter(name=uname).count()

    if upwd != cpwd:

        # messages.error(request,'两次输入密码不同，请重新输入')

        return redirect('/user/register.html')

    elif count == 1:

        #用户名重复

        return redirect('/user/register.html')

    else:

       user = User()

       user.name = uname

       user.password = upwd

       user.save()

       return redirect('/user/signin.html')

def signinHandle(request):

    post = request.POST

    uname = post.get('user_name')

    upwd = post.get('pwd')

    list = User.objects.filter(name=uname)

    if upwd != list[0].password:

        #用户名或密码错误

        return redirect('/user/register.html')

    else:

        request.session['uname'] = uname
        request.session['sex'] = list[0].sex
        request.session['work'] = list[0].work
        request.session['birth'] = list[0].birth
        request.session['ad'] = list[0].address
        request.session['desc'] = list[0].desc

        return redirect('/user/gerenyemian.html')

def infoHandle(request):

    uname = request.POST['user_name']
    user = User()
    list = User.objects.filter(name=uname)
    user = list[0]
    response_data = {}
    response_data['uname'] = user.name = uname
    response_data['sex'] = user.sex = request.POST['sex']
    response_data['work'] = user.work = request.POST['work']
    response_data['birth'] = user.birth = request.POST['birth']
    response_data['ad'] = user.address = request.POST['ad']
    response_data['desc'] = user.desc = request.POST['desc']
    user.save()
    # return HttpResponse(json.dumps(response_data), content_type="application/json")
    # return JsonResponse(response_data)
    return render(request, 'users/gerenyemian.html', response_data)
    # return HttpResponse(user.desc)