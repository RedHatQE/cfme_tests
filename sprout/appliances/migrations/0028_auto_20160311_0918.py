# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 09:18


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0027_auto_20160310_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliancepool',
            name='version',
            field=models.CharField(help_text=b'Appliance version', max_length=32, null=True),
        ),
    ]
