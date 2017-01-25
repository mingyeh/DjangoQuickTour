# encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from blog.models import *

def index(reqeust):
    template = loader.get_template('blog/index.html')
    allArticles = Article.objects.all().order_by('-timestamp')
    context = {
        'all_articles' : allArticles,
    }
    return HttpResponse(template.render(context, reqeust))