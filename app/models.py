from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Product(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像')
    thumbnail = models.ImageField(upload_to='images', verbose_name='サムネイル', null=True, blank=True)
    url = models.CharField('URL', max_length=100, null=True, blank=True)
    created = models.DateField('作成日時')
    description = models.TextField('説明')

    def __str__(self):
        return self.title



class Blog(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField("タイトル", max_length=200)
	image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
	content = models.TextField("本文")
	created = models.DateTimeField("作成日", default=timezone.now)
category = models.CharField(max_length=255,default='VR')

def __str__(self):
        return self.title


class Caregory(models.Model):
    name=models.CharField(max_length=255)

def __str__(self):
    return self.title