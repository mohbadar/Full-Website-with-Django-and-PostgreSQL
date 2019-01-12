# Generated by Django 2.1.2 on 2019-01-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_management', '0003_auto_20190108_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(help_text='Slug will be generated automatically from the title of the post', unique=True),
        ),
    ]