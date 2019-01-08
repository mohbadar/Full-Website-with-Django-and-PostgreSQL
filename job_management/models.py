from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import  RichTextUploadingField
# Create your models here.

# category model class
class JobCategory(models.Model):
	name = models.CharField(max_length=128, verbose_name=('Category Name'))
	desc = models.TextField(blank=True, default='',verbose_name=('Category Description'))
	created_at = models.DateTimeField(default=timezone.now, editable=False)


	def __str__(self):
		return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.name)

	class Meta:
		ordering = ['-created_at']


class Entity(models.Model):
    name= models.CharField(max_length=128, verbose_name=("Entity Name"))
    slug = models.CharField(max_length=120, unique=True, blank=True, help_text="Slug will be generated automatically")
    description = RichTextUploadingField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "{} : {} ".format(self.created_at.strftime('%Y-%m-%d'), self.name)

    class Meta:
        ordering = ['-created_at']


class Job(models.Model):
    title = models.TextField(max_length=512, verbose_name=("Job Title"))
    entity = models.ForeignKey(Entity, related_name="job_entity", verbose_name=("Entity"), on_delete="cascade")
    description = RichTextUploadingField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    publish_date = models.DateTimeField(verbose_name=("Publish Date"))
    expire_date  = models.DateTimeField(verbose_name=("Expiration Date"))

    def __str__(self):
        return "{} : {} : {}".format(self.publish_date.strftime('%Y-%m-%d'), self.title, self.expire_date)

    class Meta:
        ordering = ['-expire_date']

