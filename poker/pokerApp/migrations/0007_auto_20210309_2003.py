# Generated by Django 3.1.7 on 2021-03-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerApp', '0006_auto_20210309_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='password',
            field=models.CharField(default='pestillo01', max_length=30),
        ),
    ]
