# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-24 06:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Store', '0001_initial'),
        ('GoodsType', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品编号')),
                ('name', models.CharField(max_length=255, verbose_name='商品名称')),
                ('price', models.IntegerField(verbose_name='商品单价')),
                ('stock', models.IntegerField(verbose_name='商品库存')),
                ('count', models.IntegerField(verbose_name='销售数量')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='上架时间')),
                ('desc', tinymce.models.HTMLField(verbose_name='商品介绍')),
                ('goods_detail_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GoodsType.GoodsType', verbose_name='商品类型')),
                ('goods_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.Store', verbose_name='所属店铺')),
            ],
        ),
    ]
