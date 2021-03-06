# Generated by Django 2.1.2 on 2020-11-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adra', '0030_remove_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_10_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Fruta en conserva'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_11_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Tarritos infantiles con pollo'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_12_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Tarritos infantiles de fruta'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_13_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Leche entera UHT'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_14_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Batidos de chocolate'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_15_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Aceite de oliva'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_1_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Arroz Blanco'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_2_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Alubia cocida'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_3_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Conserva de at??n'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_4_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Conserva de sardina'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_6_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Pasta alimenticia tipo macarr??n'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_7_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Tomate frito en conserva'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_8_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Galletas'),
        ),
        migrations.AlterField(
            model_name='almacenalimentos',
            name='alimento_9_caducidad',
            field=models.DateField(blank=True, default=None, verbose_name='Macedonia de verduras en conserva'),
        ),
    ]
