# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_remove_userworkers_nameworker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranexoparque',
            name='I2',
        ),
        migrations.RemoveField(
            model_name='usercompany',
            name='revision',
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to=b'users', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I1',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I10',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I11',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I12',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I13',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I14',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I15',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I16',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I17',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I18',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I19',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I20',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I21',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I22',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I23',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I24',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I25',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I26',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I27',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I28',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I29',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I3',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I30',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I4',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I5',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I6',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I7',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I8',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='I9',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='IA',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexoparque',
            name='IB',
            field=models.FileField(upload_to=b'anexosParque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F1',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F10',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F11',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F12',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F13',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F14',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F15',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F16',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F17',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F18',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F19',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F2',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F20',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F21',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F22',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F23',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F24',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F25',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F26',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F27',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F3',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F4',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F5',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F6',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F7',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F8',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='F9',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='FA',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranexotrobajo',
            name='FB',
            field=models.FileField(upload_to=b'anexosTR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usercompany',
            name='activity',
            field=models.CharField(max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdocs',
            name='TC2',
            field=models.FileField(upload_to=b'TC2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdocs',
            name='notETT',
            field=models.FileField(upload_to=b'notETT', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdocs',
            name='protection',
            field=models.FileField(upload_to=b'protection', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdocs',
            name='risk',
            field=models.FileField(upload_to=b'risk', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdocs',
            name='safe',
            field=models.FileField(upload_to=b'safe', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdocs',
            name='ssocial',
            field=models.FileField(upload_to=b'ssocial', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userworkers',
            name='EPI_doc',
            field=models.FileField(upload_to=b'EPI', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userworkers',
            name='TA2_doc',
            field=models.FileField(upload_to=b'usuarios', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userworkers',
            name='information_doc',
            field=models.FileField(upload_to=b'information', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userworkers',
            name='medical_doc',
            field=models.FileField(upload_to=b'medical', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userworkers',
            name='skill_doc',
            field=models.FileField(upload_to=b'skill', blank=True),
            preserve_default=True,
        ),
    ]