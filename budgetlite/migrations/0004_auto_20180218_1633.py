# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-18 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetlite', '0003_auto_20180218_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='tag',
            field=models.CharField(choices=[('Gas', 'Gas'), ('2', 'Food'), ('Fun', 'Fun'), ('4', 'Extras'), ('5', 'Contas')], max_length=25),
        ),
    ]
