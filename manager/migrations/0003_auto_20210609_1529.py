# Generated by Django 3.1.4 on 2021-06-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_manager_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='country',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='manager',
            name='ip',
            field=models.TextField(default=''),
        ),
    ]
