#coding=utf-8
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date = models.DateField()
    readings = models.BigIntegerField()

    def __str__(self):
        return "%s"%self.content

    def __str__(self):
        return "%s" % self.title

