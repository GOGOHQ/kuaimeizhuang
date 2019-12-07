# Generated by Django 2.0 on 2019-12-05 08:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Colorspecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('r', models.IntegerField(validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)])),
                ('g', models.IntegerField(validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)])),
                ('b', models.IntegerField(validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('picUrl', models.CharField(max_length=150)),
                ('sketch', models.TextField(max_length=40)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Category')),
                ('colorspecies', models.ManyToManyField(to='Product.Colorspecies')),
            ],
        ),
    ]