# Generated by Django 3.1.7 on 2021-03-10 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerApp', '0007_auto_20210309_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='players',
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]
