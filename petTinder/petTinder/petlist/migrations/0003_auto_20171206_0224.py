# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petlist', '0002_auto_20171205_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='pet_photo',
            field=models.ImageField(upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='pet_photo2',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='pet_photo3',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='pet_photo4',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='pet_photo5',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='pet_photo6',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]