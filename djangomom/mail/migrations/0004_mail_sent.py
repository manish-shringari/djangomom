# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-10 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_remove_mail_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='sent',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]