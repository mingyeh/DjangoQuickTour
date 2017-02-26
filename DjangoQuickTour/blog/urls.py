from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<archiveYear>[\d]{4})/(?P<archiveMonth>[\d]{2})/(?P<pageNo>[\d]+)', views.archiveInPages, name = 'archiveInPages'),
    url(r'^(?P<archiveYear>[\d]{4})/(?P<archiveMonth>[\d]{2})', views.archive, name = 'archive'),
    url(r'^(?P<pageNo>[\d]+)',views.indexInPages, name = 'indexInPages'),
    url(r'^category/(?P<categoryID>[\d]+)/(?P<pageNo>[\d]+)', views.categoryInPages, name = 'categoryInPages'),
    url(r'^category/(?P<categoryID>[\d]+)', views.category, name = 'category'),
    url(r'^article/(?P<articleID>[\d]+)', views.article, name = 'article'),
]