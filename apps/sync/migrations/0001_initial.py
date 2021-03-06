# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-26 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('ingr', models.TextField(null=True)),
                ('url', models.TextField(null=True)),
                ('serves', models.IntegerField(null=True)),
                ('love', models.ManyToManyField(related_name='lovedRecipes', to='login.User')),
                ('user', models.ManyToManyField(related_name='userRecipes', to='login.User')),
            ],
        ),
    ]
