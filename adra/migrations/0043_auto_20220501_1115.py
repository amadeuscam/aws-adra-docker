# Generated by Django 3.2.10 on 2022-05-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adra', '0042_auto_20220501_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='almacenalimentos',
            name='alimento_13',
            field=models.IntegerField(default=None, verbose_name='Aceite de oliva'),
        ),
        migrations.AddField(
            model_name='almacenalimentos',
            name='alimento_13_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Aceite de oliva'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_1',
            field=models.IntegerField(default=None, verbose_name='Arroz Blanco'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_10',
            field=models.IntegerField(default=None, verbose_name='Tarritos infantiles con pollo'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_10_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Tarritos infantiles con pollo'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_11',
            field=models.IntegerField(default=None, verbose_name='Tarritos infantiles de fruta'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_11_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Tarritos infantiles de fruta'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_12',
            field=models.IntegerField(default=None, verbose_name='Leche entera UHT'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_12_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Leche entera UHT'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_2',
            field=models.IntegerField(default=None, verbose_name='Alubia cocida'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_2_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Alubia cocida'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_3',
            field=models.IntegerField(default=None, verbose_name='Conserva de at??n'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_4',
            field=models.IntegerField(default=None, verbose_name='Pasta alimenticia tipo macarron'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_4_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Pasta alimenticia tipo macarron'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_5',
            field=models.IntegerField(default=None, verbose_name='Tomate frito en conserva'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_6',
            field=models.IntegerField(default=None, verbose_name='Galletas'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_7',
            field=models.IntegerField(default=None, verbose_name='Macedonia de verduras en conserva'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_8',
            field=models.IntegerField(default=None, verbose_name='Fruta en conserva'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_8_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Fruta en conserva'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_9',
            field=models.IntegerField(default=None, verbose_name='Cacao soluble'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_9_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Cacao soluble'),
        ),
    ]
