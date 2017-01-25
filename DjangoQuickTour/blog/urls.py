from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<pageNo>[\d]+)',views.indexInPages, name = 'indexInPages'),
    url(r'^article/(?P<articleID>[\d]+)', views.article, name='article'),
]