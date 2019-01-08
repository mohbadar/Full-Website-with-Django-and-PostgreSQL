from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import  RichTextUploadingField
# Create your models here.

# category model class
class EventCategory(models.Model):
	name = models.CharField(max_length=128, verbose_name=('Category Name'))
	desc = models.TextField(blank=True, default='',verbose_name=('Category Description'))
	created_at = models.DateTimeField(default=timezone.now, editable=False)


	def __str__(self):
		return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.name)

	class Meta:
		ordering = ['-created_at']




class Event(models.Model):
	category = models.ForeignKey(EventCategory, related_name='event_category' , on_delete='cascade')
	created_at = models.DateTimeField(default=timezone.now, editable=False)
	title = models.CharField(max_length=512)
	source = models.CharField(max_length=128,blank=True)
	slug = models.CharField(max_length=120, unique=True,default=title, blank=True, help_text="Slug will be generated automatically from the title of the post")
	pub_date = models.DateTimeField(auto_now_add=True)
	content = RichTextUploadingField()

	def __str__(self):
		return '{}: {}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.title, self.category)

	class Meta:
		ordering = ['-created_at']



class EventComment(models.Model):
    name = models.CharField(max_length=128, verbose_name=("Your Name"))
    phone = models.CharField(max_length=13, verbose_name=("Your Phone"), blank=True)
    email = models.CharField(max_length=64, verbose_name=("Your E-Mail"), blank=True)
    comment = models.TextField(max_length=512, verbose_name=("Your Comment"))
    event = models.ForeignKey(Event, related_name="event", on_delete="cascade")
    created_at = models.DateTimeField(default=timezone.now, editable=False)


    def __str__(self):
        return "{} : {} : {} ".format(self.created_at.strftime('%Y-%m-%d'), self.name, self.phone)

    class Meta:
        ordering = ['-created_at']

