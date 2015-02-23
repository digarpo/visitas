# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20141202_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userworkers',
            name='nameWorker',
        ),
    ]
