from django.contrib import admin
from .models import News, NewsCateory, NewsSource

# Register your models here.

admin.site.register(NewsCateory)
admin.site.register(NewsSource)
admin.site.register(News)
