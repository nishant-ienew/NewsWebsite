# Generated by Django 3.1.4 on 2020-12-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201223_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='tw',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='yt',
            field=models.TextField(default='-'),
        ),
    ]
