# Generated by Django 2.2.6 on 2019-10-20 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0013_auto_20191020_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='observacion',
            field=models.CharField(default='Ninguna..', max_length=200),
        ),
    ]