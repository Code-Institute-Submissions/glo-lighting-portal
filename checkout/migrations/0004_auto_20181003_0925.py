# Generated by Django 2.0.6 on 2018-10-03 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20180928_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='product_id',
            new_name='product',
        ),
    ]