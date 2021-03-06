# Generated by Django 2.0.6 on 2018-09-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180911_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fitting',
            field=models.CharField(blank=True, choices=[('X', 'fitting'), ('E27', 'E27'), ('E16', '16'), ('GU10', 'GU10'), ('LED built in', 'LED built in')], default='X', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, choices=[('X', 'material'), ('metal sprayed copper', 'metal sprayed copper'), ('metal sprayed silver', 'metal sprayed silver'), ('metal', 'metal'), ('aluminium', 'aluminium'), ('copper', 'copper'), ('vineer', 'vineer'), ('fibreglass', 'fibreglass')], default='X', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('X', 'choose type'), ('suspension', 'suspension'), ('floor', 'floor'), ('table', 'table'), ('wall-ceiling', 'wall-ceiling'), ('recessed', 'recessed'), ('outside', 'outside')], default='X', max_length=15),
        ),
    ]
