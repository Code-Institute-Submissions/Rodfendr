# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-14 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
