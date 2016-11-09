# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drip',
            name='reply_to',
            field=models.EmailField(blank=True, max_length=254, help_text='Set a custom reply-to email.', null=True),
        ),
        migrations.AddField(
            model_name='sentdrip',
            name='reply_to',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
    ]
