# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_filepicker.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', django_filepicker.models.FPFileField(blank=True, null=True, upload_to='')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name='URL')),
                ('html', models.TextField(blank=True, null=True, verbose_name='HTML')),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('home_01', 'Homepage (after Features)'), ('sidebar', 'Sidebar')], max_length=30)),
                ('order', models.PositiveIntegerField(default=0)),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placements', to='advertising.Advert')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='placement',
            unique_together=set([('region', 'advert')]),
        ),
    ]
