# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20150818_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='es_superusuario',
            new_name='is_staff',
        ),
    ]
