# Generated by Django 3.2.10 on 2022-05-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adra', '0041_alter_alimentos_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimentos',
            name='alimento_13',
            field=models.IntegerField(default=None, verbose_name='Aceite de oliva'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='alimento_10',
            field=models.IntegerField(default=None, verbose_name='Tarritos infantiles con pollo'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='alimento_11',
            field=models.IntegerField(default=None, verbose_name='Tarritos infantiles de fruta'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='alimento_12',
            field=models.IntegerField(default=None, verbose_name='Leche entera UHT'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='alimento_2',
            field=models.IntegerField(default=None, verbose_name='Alubia cocida'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='alimento_4',
            field=models.IntegerField(default=None, verbose_name='Pasta alimenticia tipo macarron'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='alimento_8',
            field=models.IntegerField(default=None, verbose_name='Fruta en conserva'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='alimento_9',
            field=models.IntegerField(default=None, verbose_name='Cacao soluble'),
        ),
    ]
