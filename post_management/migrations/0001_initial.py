# Generated by Django 2.1.2 on 2019-01-07 18:07

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('title', models.CharField(max_length=512)),
                ('source', models.CharField(blank=True, max_length=128)),
                ('slug', models.CharField(blank=True, default=models.CharField(max_length=512), help_text='Slug will be generated automatically from the title of the post', max_length=120, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Category Name')),
                ('desc', models.TextField(blank=True, default='', verbose_name='Category Description')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Your Name')),
                ('phone', models.CharField(blank=True, max_length=13, verbose_name='Your Phone')),
                ('email', models.CharField(blank=True, max_length=64, verbose_name='Your E-Mail')),
                ('comment', models.TextField(max_length=512, verbose_name='Your Comment')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('event', models.ForeignKey(on_delete='cascade', related_name='event', to='post_management.Post')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete='cascade', related_name='post_category', to='post_management.PostCategory'),
        ),
    ]
