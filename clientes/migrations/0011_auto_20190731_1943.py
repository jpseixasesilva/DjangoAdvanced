# Generated by Django 2.0.1 on 2019-07-31 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_remove_venda_produtos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itensdopedido',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='itensdopedido',
            name='venda',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='pessoa',
        ),
        migrations.DeleteModel(
            name='ItensDoPedido',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.DeleteModel(
            name='Venda',
        ),
    ]
