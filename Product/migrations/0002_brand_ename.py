# Generated by Django 2.0 on 2019-12-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='ename',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
