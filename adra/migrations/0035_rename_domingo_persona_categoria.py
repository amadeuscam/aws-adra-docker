# Generated by Django 3.2.10 on 2022-01-23 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adra', '0034_alter_persona_ciudad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='domingo',
            new_name='categoria',
        ),
    ]