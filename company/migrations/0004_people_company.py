# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 06:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_remove_people_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.Company'),
            preserve_default=False,
        ),
    ]