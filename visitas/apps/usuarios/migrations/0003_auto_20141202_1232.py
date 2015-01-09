# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0003_auto_20141126_1505'),
        ('admin', '0001_initial'),
        ('usuarios', '0002_auto_20141126_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercoordinate',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='UserCoordinate',
        ),
    ]
