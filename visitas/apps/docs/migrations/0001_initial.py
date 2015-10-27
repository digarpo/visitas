# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('validate', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_doc', models.CharField(default=b'FA', max_length=2, choices=[(b'FA', b'FA'), (b'FB', b'FB'), (b'F1', b'F1'), (b'F2', b'F2'), (b'F3', b'F3'), (b'F4', b'F4'), (b'F5', b'F5'), (b'F6', b'F6'), (b'F7', b'F7'), (b'F8', b'F8'), (b'F9', b'F9'), (b'F10', b'F10'), (b'F11', b'F11'), (b'F12', b'F12'), (b'F13', b'F13'), (b'F14', b'F14'), (b'F15', b'F15'), (b'F16', b'F16'), (b'F17', b'F17'), (b'F18', b'F18'), (b'F19', b'F19'), (b'F20', b'F20'), (b'F21', b'F21'), (b'F22', b'F22'), (b'F23', b'F23'), (b'F24', b'F24'), (b'F25', b'F25'), (b'F26', b'F26'), (b'IA', b'IA'), (b'IB', b'IB'), (b'I1', b'I1'), (b'I2', b'I2'), (b'I3', b'I3'), (b'I4', b'I4'), (b'I5', b'I5'), (b'I6', b'I6'), (b'I7', b'I7'), (b'IA8', b'IA8'), (b'IA9', b'IA9'), (b'IA10', b'IA10'), (b'IA11', b'IA11'), (b'IA12', b'IA12'), (b'IA13', b'IA13'), (b'IA14', b'IA14'), (b'IA15', b'IA15'), (b'IA16', b'IA16'), (b'IA17', b'IA17'), (b'IA18', b'IA18'), (b'IA19', b'IA19'), (b'IA20', b'IA20'), (b'IA20', b'IA20'), (b'IA21', b'IA21'), (b'IA22', b'IA22'), (b'IA23', b'IA23'), (b'IA24', b'IA24'), (b'IA25', b'IA25'), (b'IA26', b'IA26'), (b'IA27', b'IA27'), (b'IA28', b'IA28'), (b'IA29', b'IA29'), (b'IA30', b'IA30')])),
                ('read', models.BooleanField(default=False)),
                ('doc', models.ForeignKey(to='docs.Docs')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
