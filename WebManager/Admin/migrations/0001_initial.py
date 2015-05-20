# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024)),
                ('posted', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=128)),
                ('notes', models.TextField()),
                ('started', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('data', models.TextField()),
                ('campaign', models.ForeignKey(to='Admin.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trust', models.IntegerField(default=0)),
                ('salary', models.FloatField()),
                ('type', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmployeeHash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(max_length=16)),
                ('trust', models.IntegerField(default=0)),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('type', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('taken', models.DateTimeField(null=True, blank=True)),
                ('type', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('flags', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(unique=True, max_length=2048)),
                ('ems', models.IntegerField()),
                ('cpc', models.FloatField()),
                ('difficulty', models.FloatField()),
                ('discarded', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('type', models.CharField(max_length=64)),
                ('niche', models.TextField()),
                ('notes', models.TextField()),
                ('user', models.CharField(max_length=64)),
                ('pw', encrypted_fields.fields.EncryptedTextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='job',
            name='keywords',
            field=models.ManyToManyField(to='Admin.Keyword', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='taker',
            field=models.ForeignKey(blank=True, to='Admin.Employee', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='site',
            field=models.ForeignKey(to='Admin.Site'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='Admin.Employee'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.ManyToManyField(to='Admin.Keyword', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='site',
            field=models.ForeignKey(blank=True, to='Admin.Site', null=True),
            preserve_default=True,
        ),
    ]
