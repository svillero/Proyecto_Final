# Generated by Django 4.0.6 on 2022-08-31 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmensajes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='numero',
        ),
    ]
