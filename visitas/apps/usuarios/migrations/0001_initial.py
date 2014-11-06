# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to=b'users')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAnexoParque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IA', models.FileField(upload_to=b'anexosParque')),
                ('IB', models.FileField(upload_to=b'anexosParque')),
                ('I1', models.FileField(upload_to=b'anexosParque')),
                ('I2', models.FileField(upload_to=b'anexosParque')),
                ('I3', models.FileField(upload_to=b'anexosParque')),
                ('I4', models.FileField(upload_to=b'anexosParque')),
                ('I5', models.FileField(upload_to=b'anexosParque')),
                ('I6', models.FileField(upload_to=b'anexosParque')),
                ('I7', models.FileField(upload_to=b'anexosParque')),
                ('I8', models.FileField(upload_to=b'anexosParque')),
                ('I9', models.FileField(upload_to=b'anexosParque')),
                ('I10', models.FileField(upload_to=b'anexosParque')),
                ('I11', models.FileField(upload_to=b'anexosParque')),
                ('I12', models.FileField(upload_to=b'anexosParque')),
                ('I13', models.FileField(upload_to=b'anexosParque')),
                ('I14', models.FileField(upload_to=b'anexosParque')),
                ('I15', models.FileField(upload_to=b'anexosParque')),
                ('I16', models.FileField(upload_to=b'anexosParque')),
                ('I17', models.FileField(upload_to=b'anexosParque')),
                ('I18', models.FileField(upload_to=b'anexosParque')),
                ('I19', models.FileField(upload_to=b'anexosParque')),
                ('I20', models.FileField(upload_to=b'anexosParque')),
                ('I21', models.FileField(upload_to=b'anexosParque')),
                ('I22', models.FileField(upload_to=b'anexosParque')),
                ('I23', models.FileField(upload_to=b'anexosParque')),
                ('I24', models.FileField(upload_to=b'anexosParque')),
                ('I25', models.FileField(upload_to=b'anexosParque')),
                ('I26', models.FileField(upload_to=b'anexosParque')),
                ('I27', models.FileField(upload_to=b'anexosParque')),
                ('I28', models.FileField(upload_to=b'anexosParque')),
                ('I29', models.FileField(upload_to=b'anexosParque')),
                ('I30', models.FileField(upload_to=b'anexosParque')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAnexoTrobajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FA', models.FileField(upload_to=b'anexosTR')),
                ('FB', models.FileField(upload_to=b'anexosTR')),
                ('F1', models.FileField(upload_to=b'anexosTR')),
                ('F2', models.FileField(upload_to=b'anexosTR')),
                ('F3', models.FileField(upload_to=b'anexosTR')),
                ('F4', models.FileField(upload_to=b'anexosTR')),
                ('F5', models.FileField(upload_to=b'anexosTR')),
                ('F6', models.FileField(upload_to=b'anexosTR')),
                ('F7', models.FileField(upload_to=b'anexosTR')),
                ('F8', models.FileField(upload_to=b'anexosTR')),
                ('F9', models.FileField(upload_to=b'anexosTR')),
                ('F10', models.FileField(upload_to=b'anexosTR')),
                ('F11', models.FileField(upload_to=b'anexosTR')),
                ('F12', models.FileField(upload_to=b'anexosTR')),
                ('F13', models.FileField(upload_to=b'anexosTR')),
                ('F14', models.FileField(upload_to=b'anexosTR')),
                ('F15', models.FileField(upload_to=b'anexosTR')),
                ('F16', models.FileField(upload_to=b'anexosTR')),
                ('F17', models.FileField(upload_to=b'anexosTR')),
                ('F18', models.FileField(upload_to=b'anexosTR')),
                ('F19', models.FileField(upload_to=b'anexosTR')),
                ('F20', models.FileField(upload_to=b'anexosTR')),
                ('F21', models.FileField(upload_to=b'anexosTR')),
                ('F22', models.FileField(upload_to=b'anexosTR')),
                ('F23', models.FileField(upload_to=b'anexosTR')),
                ('F24', models.FileField(upload_to=b'anexosTR')),
                ('F25', models.FileField(upload_to=b'anexosTR')),
                ('F26', models.FileField(upload_to=b'anexosTR')),
                ('F27', models.FileField(upload_to=b'anexosTR')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCentral',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('plant', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('usuarios.user',),
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=7)),
                ('mobile', models.CharField(max_length=7)),
                ('CIF', models.CharField(max_length=100)),
                ('activity', models.CharField(max_length=500)),
                ('revision', models.DateTimeField()),
                ('subcontrate', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('usuarios.user',),
        ),
        migrations.CreateModel(
            name='UserCoordinate',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('usuarios.user',),
        ),
        migrations.CreateModel(
            name='UserDepartment',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('departament', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('usuarios.user',),
        ),
        migrations.CreateModel(
            name='UserDocs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TC2', models.FileField(upload_to=b'TC2')),
                ('safe', models.FileField(upload_to=b'safe')),
                ('ssocial', models.FileField(upload_to=b'ssocial')),
                ('notETT', models.FileField(upload_to=b'notETT')),
                ('risk', models.FileField(upload_to=b'risk')),
                ('protection', models.FileField(upload_to=b'protection')),
                ('ICCo', models.CharField(max_length=100)),
                ('ICSyva', models.CharField(max_length=100)),
                ('PRL03', models.CharField(max_length=100)),
                ('PRL04', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserWorkers',
            fields=[
                ('usercompany_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='usuarios.UserCompany')),
                ('nameWorker', models.CharField(max_length=100)),
                ('TA2_date', models.DateTimeField()),
                ('TA2_doc', models.FileField(upload_to=b'usuarios')),
                ('medical', models.DateTimeField()),
                ('information', models.DateTimeField()),
                ('formation_date', models.DateTimeField()),
                ('EPI_date', models.DateTimeField()),
                ('EPI_doc', models.FileField(upload_to=b'EPI')),
                ('medical_doc', models.FileField(upload_to=b'medical')),
                ('information_doc', models.FileField(upload_to=b'information')),
                ('skill_doc', models.FileField(upload_to=b'skill')),
            ],
            options={
                'abstract': False,
            },
            bases=('usuarios.usercompany',),
        ),
        migrations.AddField(
            model_name='userdocs',
            name='user',
            field=models.ForeignKey(to='usuarios.UserWorkers', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='useranexotrobajo',
            name='user',
            field=models.ForeignKey(to='usuarios.UserCompany', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='useranexoparque',
            name='user',
            field=models.ForeignKey(to='usuarios.UserCompany', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
