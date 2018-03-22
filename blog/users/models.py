from django.db import models
import datetime
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    sex = models.CharField(max_length=1,default='')
    work = models.CharField(max_length=10,default='')
    birth = models.CharField(max_length=11,default='')
    address = models.CharField(max_length=50,default='')
    headImg = models.ImageField(upload_to='upload/')
    desc = models.TextField(max_length=200,default='')

    def __str__(self):
        return "%s" % self.work

    def __str__(self):
        return "%s" % self.address

    def __str__(self):
        return "%s" % self.desc

    def __str__(self):
        return "%s"%self.birth

    def __str__(self):
        return "%s" % self.name
