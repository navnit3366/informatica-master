# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-02 21:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0008_auto_20170102_2131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='following_count',
            new_name='followed_count',
        ),
    ]
