# Generated by Django 3.2.10 on 2022-01-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adra', '0033_auto_20220122_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='ciudad',
            field=models.CharField(max_length=350),
        ),
    ]
