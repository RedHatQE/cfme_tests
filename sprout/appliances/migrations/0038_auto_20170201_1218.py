# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-01 12:18


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0037_auto_20170131_1058_squashed_0043_auto_20170131_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='cpu_limit',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='custom_cpu_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='custom_memory_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='memory_limit',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='total_cpu',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='total_memory',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='used_cpu',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='used_memory',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
