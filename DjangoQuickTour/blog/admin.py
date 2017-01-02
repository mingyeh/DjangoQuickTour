from django.contrib import admin
from blog.models import *

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp')
	list_filter = ['timestamp']
	search_fields = ['title']

admin.site.register(Article, ArticleAdmin)
