# Generated by Django 2.0.6 on 2020-01-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20200104_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='name',
            field=models.CharField(max_length=64, verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='name',
            field=models.CharField(max_length=64, verbose_name='项目名称'),
        ),
    ]
