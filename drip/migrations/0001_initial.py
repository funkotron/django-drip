# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text=b'A unique name for this drip.', max_length=255, unique=True, verbose_name=b'Drip Name')),
                ('enabled', models.BooleanField(default=False)),
                ('from_email', models.EmailField(blank=True, help_text=b'Set a custom from email.', max_length=254, null=True)),
                ('from_email_name', models.CharField(blank=True, help_text=b'Set a name for a custom from email.', max_length=150, null=True)),
                ('subject_template', models.TextField(blank=True, null=True)),
                ('body_html_template', models.TextField(blank=True, help_text=b'You will have settings and user in the context.', null=True)),
                ('message_class', models.CharField(blank=True, default=b'default', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='QuerySetRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('method_type', models.CharField(choices=[(b'filter', b'Filter'), (b'exclude', b'Exclude')], default=b'filter', max_length=12)),
                ('field_name', models.CharField(max_length=128, verbose_name=b'Field name of User')),
                ('lookup_type', models.CharField(choices=[(b'exact', b'exactly'), (b'iexact', b'exactly (case insensitive)'), (b'contains', b'contains'), (b'icontains', b'contains (case insensitive)'), (b'regex', b'regex'), (b'iregex', b'contains (case insensitive)'), (b'gt', b'greater than'), (b'gte', b'greater than or equal to'), (b'lt', b'less than'), (b'lte', b'less than or equal to'), (b'startswith', b'starts with'), (b'endswith', b'starts with'), (b'istartswith', b'ends with (case insensitive)'), (b'iendswith', b'ends with (case insensitive)')], default=b'exact', max_length=12)),
                ('field_value', models.CharField(help_text=b'Can be anything from a number, to a string. Or, do `now-7 days` or `today+3 days` for fancy timedelta.', max_length=255)),
                ('drip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queryset_rules', to='drip.Drip')),
            ],
        ),
        migrations.CreateModel(
            name='SentDrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('subject', models.TextField()),
                ('body', models.TextField()),
                ('from_email', models.EmailField(default=None, max_length=254, null=True)),
                ('from_email_name', models.CharField(default=None, max_length=150, null=True)),
                ('drip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_drips', to='drip.Drip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_drips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
