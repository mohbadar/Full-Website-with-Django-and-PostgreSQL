from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import  RichTextUploadingField
# Create your models here.

# category model class
class PageCategory(models.Model):
	name = models.CharField(max_length=128, verbose_name=('Category Name'))
	desc = models.TextField(blank=True, default='',verbose_name=('Category Description'))
	created_at = models.DateTimeField(default=timezone.now, editable=False)


	def __str__(self):
		return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.name)

	class Meta:
		ordering = ['-created_at']

class Page(models.Model):
    title = models.CharField(max_length=256, verbose_name=("Page Title"))
    category = models.ForeignKey(PageCategory, related_name="page_category", on_delete="cascade")
    content  = RichTextUploadingField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    class Meta:
        ordering = ['-created_at']


class Feedback(models.Model):
    name = models.CharField(max_length=128, verbose_name=("Your Name"))
    phone = models.CharField(max_length=13, verbose_name=("Your Phone"), blank=True)
    email = models.CharField(max_length=64, verbose_name=("Your E-Mail"), blank=True)
    feedback = models.TextField(max_length=1028, verbose_name=("Your Feedback"))
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "{} : {} : {}".format(self.created_at.strftime('%Y-%m-%d'), self.name, self.phone)

    class Meta:
        ordering = ['-created_at']

        
