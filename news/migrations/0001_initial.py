# Generated by Django 3.1.4 on 2020-12-25 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-', max_length=50)),
                ('short_txt', models.TextField(default='-')),
                ('body_txt', models.TextField(default='-')),
                ('date', models.CharField(default='-', max_length=12)),
                ('writer', models.CharField(default='-', max_length=50)),
                ('pic', models.TextField()),
            ],
        ),
    ]
