# Generated by Django 2.1.2 on 2019-01-07 16:50

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Book Title')),
                ('isbn', models.CharField(blank=True, max_length=128, verbose_name='Book ISBN')),
                ('publisher', models.TextField(max_length=512, verbose_name='Publishing Details')),
                ('slug', models.CharField(blank=True, max_length=256, verbose_name='Slug')),
                ('pdf', models.FileField(blank=True, upload_to='', verbose_name='PDF of Book')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=128, verbose_name='Last Name')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('biography', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BookCateory',
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
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, on_delete='cascade', related_name='book_author', to='book_management.BookAuthor', verbose_name='Book Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, on_delete='cascade', related_name='book_category', to='book_management.BookCateory', verbose_name='Book Category'),
        ),
    ]
