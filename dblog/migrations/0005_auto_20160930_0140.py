# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-29 20:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dblog', '0004_auto_20160929_0002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subtopic',
            options={'ordering': ['id']},
        ),
    ]