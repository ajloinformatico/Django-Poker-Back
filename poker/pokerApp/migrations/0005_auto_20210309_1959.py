# Generated by Django 3.1.7 on 2021-03-09 19:59

from django.db import migrations, models
import pokerApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerApp', '0004_auto_20210309_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='avatar',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=pokerApp.models.upload_image),
        ),
        migrations.AlterField(
            model_name='player',
            name='matches',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='pokerApp.Match'),
        ),
    ]
