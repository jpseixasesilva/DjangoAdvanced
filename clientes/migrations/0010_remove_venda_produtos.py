# Generated by Django 2.0.1 on 2019-07-31 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_venda_nfe_emitida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='produtos',
        ),
    ]