# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('comment', models.CharField(max_length=200)),
                ('chore', models.ForeignKey(to='chores.Chore')),
            ],
        ),
        migrations.CreateModel(
            name='Roomie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='roomie',
            field=models.ForeignKey(to='chores.Roomie'),
        ),
        migrations.AddField(
            model_name='chore',
            name='events',
            field=models.ManyToManyField(to='chores.Roomie', through='chores.Event'),
        ),
    ]
