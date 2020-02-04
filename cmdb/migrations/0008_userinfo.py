# Generated by Django 2.0.6 on 2020-02-04 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0007_svninfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='姓名')),
                ('passwd', models.CharField(blank=True, max_length=64, verbose_name='密码')),
                ('email', models.CharField(blank=True, max_length=128, verbose_name='邮件')),
                ('phonenum', models.CharField(blank=True, max_length=128, verbose_name='电话')),
            ],
        ),
    ]
