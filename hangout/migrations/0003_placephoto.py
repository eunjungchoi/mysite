# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hangout', '0002_auto_20160511_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='static/hangout')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hangout.Place')),
            ],
        ),
    ]