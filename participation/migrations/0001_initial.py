# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField(verbose_name=b'dsds')),
                ('email', models.EmailField(help_text=b'A valid email address, please.', max_length=75)),
                ('phone', models.IntegerField(verbose_name=b'dssd')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
