# Generated by Django 3.1.7 on 2021-03-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerApp', '0005_auto_20210309_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='money',
            field=models.IntegerField(blank=True, default=20, null=True),
        ),
    ]
