from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):

    arcticle_list = Article.objects.all()

    context = {'list': arcticle_list}

    return render(request,'article/csdn博客/csdn.html',context)

def arctile(request):

    return render(request, 'article/csdn博客/blogArticles.html')

def geTi(request):

    return render(request, 'article/csdn博客/geTi.html')

def addArticle(request):

    return render(request, 'article/csdn博客/addArticle.html')

def test(request):

    arcticle_list = Article.objects.all()

    context = {'list':arcticle_list}

    return render(request,'article/test.html',context)