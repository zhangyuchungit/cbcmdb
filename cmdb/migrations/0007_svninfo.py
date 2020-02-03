# Generated by Django 2.0.6 on 2020-01-19 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_hostinfo_projectname'),
    ]

    operations = [
        migrations.CreateModel(
            name='svninfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='姓名')),
                ('ipinfo', models.CharField(blank=True, max_length=64, verbose_name='ip信息')),
                ('svnuser', models.CharField(blank=True, max_length=128, verbose_name='svnuser')),
                ('svnpasswd', models.CharField(blank=True, max_length=128, verbose_name='svnpasswd')),
                ('otherpasswd', models.CharField(blank=True, max_length=32, verbose_name='otherpasswd')),
                ('notices', models.CharField(blank=True, max_length=32, verbose_name='notices')),
            ],
        ),
    ]
