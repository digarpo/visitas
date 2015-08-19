# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20150220_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_homologado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
