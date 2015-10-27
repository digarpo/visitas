# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docuser',
            name='docfile',
            field=models.FileField(upload_to=b'docfile', blank=True),
            preserve_default=True,
        ),
    ]
