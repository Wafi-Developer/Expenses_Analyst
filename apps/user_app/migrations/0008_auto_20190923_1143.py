# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-23 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_merge_20190922_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='user_app.User'),
        ),
    ]
