# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 09:41


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0028_auto_20160311_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='hidden',
            field=models.BooleanField(
                default=False, help_text=b'We can hide providers if that is required.'),
        ),
    ]
