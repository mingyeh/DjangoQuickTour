# encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(reqeust):
    template = loader.get_template('blog/index.html')
    context = {
        'authorName' : '大狗',
    }
    return HttpResponse(template.render(context, reqeust))