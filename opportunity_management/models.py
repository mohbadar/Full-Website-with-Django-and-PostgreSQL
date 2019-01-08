from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import  RichTextUploadingField

# Create your models here.

# category model class
class OpportunityCategory(models.Model):
	name = models.CharField(max_length=128, verbose_name=('Category Name'))
	desc = models.TextField(blank=True, default='',verbose_name=('Category Description'))
	created_at = models.DateTimeField(default=timezone.now, editable=False)


	def __str__(self):
		return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.name)

	class Meta:
		ordering = ['-created_at']


class Opportunity(models.Model):
    title = models.CharField(max_length=256, verbose_name=("Opportunity Title"))
    category = models.ForeignKey(OpportunityCategory, related_name="opportunity_category", on_delete="cascade")
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    description = RichTextUploadingField()

    def __str__(self):
        return "{} : {} ".format(self.created_at.strftime('%Y-%m-%d'), self.title)

    class Meta:
        ordering = ['-created_at']
