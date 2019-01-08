from django.contrib import admin
from .models import Entity, Job, JobCategory
# Register your models here.

admin.site.register(JobCategory)
admin.site.register(Entity)
admin.site.register(Job)
