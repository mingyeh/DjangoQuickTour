# encoding:utf-8
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
	title = models.CharField(max_length = 100, verbose_name = '标题')
	author = models.CharField(max_length = 30, verbose_name = '作者')
	body = models.TextField(verbose_name = '内容')
	timestamp = models.DateTimeField(verbose_name = '发布日期')

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.__unicode__(self)

	class Meta:
		verbose_name = '文章'
		verbose_name_plural = '文章'
