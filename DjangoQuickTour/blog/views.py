# encoding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from blog.models import *
from django.core.paginator import Paginator
from django.db import connection
import re

def getArchiveItems():
    cursor = connection.cursor()
    # Please update this SQL script when migrating to other db
    sql = '''select distinct strftime('%Y年%m月',timestamp) postMonth,count(*) articleCount 
            from blog_article 
            group by postMonth 
            order by postMonth desc;'''
    cursor.execute(sql)

    resultList = []
    yearMonthRegEx = re.compile(r'(?P<year>[\d]{4})\D+(?P<month>[\d]{2})\D+')
    dataRows = cursor.fetchall()
    for row in dataRows:
        resultItem = archiveItem()
        resultItem.displayText = row[0]
        resultItem.articleCount = row[1]
        yearMonthMatchObject = re.match(yearMonthRegEx, row[0])
        if yearMonthMatchObject is not None:
            resultItem.year = yearMonthMatchObject.group('year')
            resultItem.month = yearMonthMatchObject.group('month')
        resultList.append(resultItem)

    return resultList

def archiveInPages(request, archiveYear, archiveMonth, pageNo):
    template = loader.get_template('blog/index.html')
    allArticles = Article.objects.all().filter(timestamp__year=archiveYear).filter(timestamp__month=archiveMonth).order_by('-timestamp')
    categories = Category.objects.all();
    archives = getArchiveItems()

    p = Paginator(allArticles, 5)
    articlesInPage = p.page(pageNo)
    context = {
        'articles' : articlesInPage,
        'categories': categories,
        'archives': archives,
        'archiveYear': archiveYear,
        'archiveMonth': archiveMonth,
    }
    return HttpResponse(template.render(context, request))

def archive(request, archiveYear, archiveMonth):
    return archiveInPages(request, archiveYear, archiveMonth, 1)

def index(request):
    return indexInPages(request,1)

def article(request, articleID):
    template = loader.get_template('blog/article.html')
    article = Article.objects.get(id = articleID)
    categories = Category.objects.all();
    archives = getArchiveItems()

    context = {
        'article': article,
        'categories':categories,
        'archives':archives,
    }
    return HttpResponse(template.render(context, request))

def indexInPages(request, pageNo):
    template = loader.get_template('blog/index.html')
    allArticles = Article.objects.all().order_by('-timestamp')
    categories = Category.objects.all();
    archives = getArchiveItems()

    p = Paginator(allArticles, 5)
    articlesInPage = p.page(pageNo)
    context = {
        'articles' : articlesInPage,
        'categories': categories,
        'archives':archives,
    }
    return HttpResponse(template.render(context, request))

def categoryInPages(request, categoryID, pageNo):
    template = loader.get_template('blog/index.html')
    cat = get_object_or_404(Category, id = categoryID)
    categories = Category.objects.all();
    archives = getArchiveItems()

    articlesInCat = Article.objects.filter(category = categoryID).order_by('-timestamp')
    p = Paginator(articlesInCat, 5)
    articlesInPage = p.page(pageNo)

    context = {
        'cat' : cat,
        'articles': articlesInPage,
        'categories' : categories,
        'archives':archives,
    }
    return HttpResponse(template.render(context, request))

def category(request, categoryID):
    return categoryInPages(request, categoryID, 1)