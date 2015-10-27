# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_auto_20150916_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranexoparque',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserAnexoParque',
        ),
        migrations.RemoveField(
            model_name='useranexotrobajo',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserAnexoTrobajo',
        ),
    ]
