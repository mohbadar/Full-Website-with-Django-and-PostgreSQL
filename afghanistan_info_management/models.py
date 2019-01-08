from article_management import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import  RichTextUploadingField

class Province(models.Model):
    name = models.CharField(max_length=128, verbose_name=("Province Name"))
    description = RichTextUploadingField()
    created_at = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ['name']


class Destrict(models.Model):
    name = models.CharField(max_length=64, verbose_name=("Destrict Name"))
    province = models.ForeignKey(Province, related_name="province", on_delete="cascade", verbose_name=("Province"))
    description = RichTextUploadingField()
    created_at =  models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return "{} : {}".format(self.province.name, self.name)

    class Meta:
        ordering = ['province']

class Area(models.Model):
    name = models.CharField(max_length=64, verbose_name=("Area Name"))
    destrict = models.ForeignKey(Province, related_name="destrict", on_delete="cascade", verbose_name=("Destrict"))
    description = RichTextUploadingField()
    created_at =  models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return "{} : {}".format(self.destrict.name, self.name)

    class Meta:
        ordering = ['destrict']
