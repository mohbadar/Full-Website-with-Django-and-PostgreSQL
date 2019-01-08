from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import  RichTextUploadingField

# Create your models here.


class BookAuthor(models.Model):

    firstname = models.CharField(max_length=128, verbose_name=("First Name"))
    lastname = models.CharField(max_length=128, verbose_name=("Last Name"))
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    biography = RichTextUploadingField()

    def __str__(self):
        return '{}: {}'.format(self.firstname, self.lastname)

    class Meta:
        ordering = ['-created_at']


# category model class
class BookCateory(models.Model):
	name = models.CharField(max_length=128, verbose_name=('Category Name'))
	desc = models.TextField(blank=True, default='',verbose_name=('Category Description'))
	created_at = models.DateTimeField(default=timezone.now, editable=False)


	def __str__(self):
		return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d'), self.name)

	class Meta:
		ordering = ['-created_at']


class Book(models.Model):
    title = models.CharField(max_length=256, verbose_name=("Book Title"))
    isbn = models.CharField(max_length=128, blank=True, verbose_name=("Book ISBN"))
    author = models.ForeignKey(BookAuthor, related_name="book_author",blank=True, verbose_name=("Book Author"), on_delete="cascade")
    category = models.ForeignKey(BookCateory, related_name="book_category", blank=True, verbose_name=("Book Category"), on_delete="cascade")
    publisher = models.TextField(verbose_name=("Publishing Details"), max_length=512)
    slug = models.CharField(verbose_name="Slug", max_length=256, blank=True)
    pdf = models.FileField(blank=True,verbose_name=("PDF of Book"))
    description = RichTextUploadingField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "{} : {}".format(self.title, self.isbn)

    class Meta:
        ordering = ['-created_at']
