from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import  RichTextUploadingField
from django.utils.text import slugify
# Create your models here.

# category model class
class NewsCateory(models.Model):
	name = models.CharField(max_length=128, verbose_name=('Category Name'), unique=True)
	desc = models.TextField(blank=True, default='',verbose_name=('Category Description'))
	created_at = models.DateTimeField(default=timezone.now, editable=False)


	def __str__(self):
		return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.name)

	class Meta:
		ordering = ['-created_at']


class NewsSource(models.Model):
	name = models.CharField(max_length=128, verbose_name=('Source Name'))
	desc = models.TextField(blank=True, default='', verbose_name=('Source Description'))
	created_at = models.DateTimeField(default=timezone.now, editable=False)
	reference = models.CharField(max_length=128, blank=True, verbose_name=('Reference'), help_text="Reference (e.g. website url, facebook_id,twitter tag,..)")

	def __str__(self):
		return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.name)

	class Meta:
		ordering = ['-created_at']




class News(models.Model):
	category = models.ForeignKey(NewsCateory, related_name='news_category' , on_delete='cascade')
	source = models.ForeignKey(NewsSource, related_name='news_source' , on_delete='cascade')
	created_at = models.DateTimeField(default=timezone.now, editable=False)
	title = models.CharField(max_length=512)
	source = models.CharField(max_length=128,blank=True)
	slug = models.SlugField(unique=True, help_text="Slug will be generated automatically from the title of the post")
	pub_date = models.DateTimeField(auto_now_add=True)
	content = RichTextUploadingField()

	def __str__(self):
		return '{}: {}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.title, self.category)

	# @models.permalink
	def get_absolute_url(self):
		return '{}'.format(self.slug)

	def _get_unique_slug(self):
		slug = slugify(self.title)
		unique_slug = slug
		num = 1
		while News.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num +=1

		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save(*args, **kwargs)



	class Meta:
		ordering = ['-created_at']



