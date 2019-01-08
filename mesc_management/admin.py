from django.contrib import admin
from .models import PageCategory, Page, Feedback
# Register your models here.

admin.site.register(Page)
admin.site.register(PageCategory)
admin.site.register(Feedback)
