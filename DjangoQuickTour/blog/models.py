# encoding:utf-8
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	name = models.CharField(max_length = 20, verbose_name = '分类名称')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.__unicode__()

	class Meta:
		verbose_name = '分类'
		verbose_name_plural = '分类'

class Article(models.Model):
	title = models.CharField(max_length = 100, verbose_name = '标题')
	author = models.CharField(max_length = 30, verbose_name = '作者')
	body = models.TextField(verbose_name = '内容')
	category = models.ForeignKey(Category, null = True, on_delete = models.SET_NULL)
	timestamp = models.DateTimeField(verbose_name = '发布日期')

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.__unicode__()

	class Meta:
		verbose_name = '文章'
		verbose_name_plural = '文章'

class archiveItem:
	displayText = ''
	year = ''
	month = ''
	articleCount = 0
