# Generated by Django 4.0.6 on 2022-09-01 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmensajes', '0006_mensaje_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='fecha_alta',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
