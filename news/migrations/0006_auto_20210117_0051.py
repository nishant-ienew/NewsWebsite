# Generated by Django 3.1.4 on 2021-01-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_ocatid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(default='-', max_length=200),
        ),
    ]