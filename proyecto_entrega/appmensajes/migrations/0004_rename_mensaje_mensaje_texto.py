# Generated by Django 4.0.6 on 2022-09-01 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmensajes', '0003_rename_leyenda_mensaje_mensaje'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='mensaje',
            new_name='texto',
        ),
    ]
