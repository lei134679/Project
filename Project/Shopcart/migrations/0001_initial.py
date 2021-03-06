# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-24 06:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopcart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='购物编号')),
                ('count', models.IntegerField(verbose_name='购买数量')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('subtotal', models.IntegerField(verbose_name='小计金额')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods', verbose_name='购物商品')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
        ),
    ]
