# Generated by Django 2.0.6 on 2020-01-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20200104_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='insertip',
            field=models.CharField(max_length=128, verbose_name='内网地址'),
        ),
    ]
