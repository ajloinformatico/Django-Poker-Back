# Generated by Django 3.1.7 on 2021-03-08 17:14

from django.db import migrations, models
import pokerApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('money', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
                ('nick', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=30)),
                ('money', models.IntegerField()),
                ('avatar', models.ImageField(upload_to=pokerApp.models.upload_image)),
                ('matches', models.ManyToManyField(to='pokerApp.Match')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(to='pokerApp.Player'),
        ),
    ]
