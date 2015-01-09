# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0002_auto_20141106_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='category',
            field=models.ForeignKey(blank=True, to='citas.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cita',
            name='finish',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cita',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'citas', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cita',
            name='organizer',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cita',
            name='start',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
