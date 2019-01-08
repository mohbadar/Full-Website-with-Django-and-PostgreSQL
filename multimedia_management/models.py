from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import  RichTextUploadingField

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(verbose_name=("Photo Title"),max_length=256)
    description = models.TextField(blank=True, verbose_name=("Photo Description"))
    image = models.ImageField(verbose_name=("Your Photo"))
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "{} : {} ".format(self.created_at.strftime('%Y-%m-%d'),self.title)

    class Meta:
        ordering = ['-created_at']

class Video(models.Model):
    title = models.CharField(max_length=256, verbose_name=("Video Title"))
    description = RichTextUploadingField
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    youtube_url  = models.CharField(verbose_name=("Youtube URL"),max_length=128)

    def __str__(self):
        return "{} : {} ".format(self.created_at.strftime('%Y-%m-%d'),self.title)

    class Meta:
        ordering = ['-created_at']


class Sound(models.Model):
    title = models.CharField(max_length=256, verbose_name=("Sound Title"))
    description = RichTextUploadingField
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    youtube_url  = models.CharField(verbose_name=("Youtube URL"),max_length=128)

    def __str__(self):
        return "{} : {} ".format(self.created_at.strftime('%Y-%m-%d'),self.title)

    class Meta:
        ordering = ['-created_at']


class Document(models.Model):
    title = models.CharField(max_length=256,verbose_name=("Document Title"))
    description = RichTextUploadingField
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    document = models.FileField(verbose_name=("Your File"))

    def __str__(self):
        return "{} : {} ".format(self.created_at.strftime('%Y-%m-%d'),self.title)

    class Meta:
        ordering = ['-created_at']
