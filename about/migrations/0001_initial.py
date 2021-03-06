# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images/logo', verbose_name='Upload logo')),
                ('slogan', models.CharField(max_length=255, verbose_name='Slogan on about us page')),
                ('about_text', models.TextField(verbose_name='Text about us')),
                ('development_icon', models.ImageField(upload_to='images/icons', verbose_name='Icon for development')),
                ('development_text', models.TextField(verbose_name='Development text')),
                ('branding_icon', models.ImageField(upload_to='images/icons', verbose_name='Icon for branding')),
                ('branding_text', models.TextField(verbose_name='Branding text')),
                ('art_icon', models.ImageField(upload_to='images/icons', verbose_name='Icon for art direction')),
                ('art_text', models.TextField(verbose_name='Text for art direction')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
    ]
