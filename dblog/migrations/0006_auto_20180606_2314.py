# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-06 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dblog', '0005_auto_20160930_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='type',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='subtopicDesc',
            field=models.TextField(),
        ),
    ]