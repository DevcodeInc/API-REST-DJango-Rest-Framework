# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tags', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=15)),
                ('zip_code', models.CharField(max_length=15)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('state', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Product')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Purchase')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='purchase',
            name='products',
            field=models.ManyToManyField(through='compras.PurchaseItem', to='compras.Product'),
        ),
    ]
