# Generated by Django 2.1.2 on 2019-01-07 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Document Title')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('document', models.FileField(upload_to='', verbose_name='Your File')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Photo Title')),
                ('description', models.TextField(blank=True, verbose_name='Photo Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Your Photo')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Sound Title')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('youtube_url', models.CharField(max_length=128, verbose_name='Youtube URL')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Video Title')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('youtube_url', models.CharField(max_length=128, verbose_name='Youtube URL')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]