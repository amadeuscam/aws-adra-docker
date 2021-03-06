# Generated by Django 3.2.10 on 2022-01-22 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adra', '0032_auto_20210620_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='otros_documentos',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre_apellido',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre del beneficiario'),
        ),
    ]
