# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20160503_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='photo',
            field=models.ImageField(default='', upload_to='company'),
            preserve_default=False,
        ),
    ]
