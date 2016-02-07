# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tracker.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic', models.FileField(null=True, upload_to=tracker.models.get_upload_file_name, blank=True)),
                ('url', models.URLField(default='https://github.com/Alsum', null=True, blank=True)),
                ('mobile', models.CharField(default='111111111111', max_length=12, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='serviceplan',
            name='user_profile',
            field=models.ForeignKey(to='tracker.UserProfile'),
        ),
    ]
