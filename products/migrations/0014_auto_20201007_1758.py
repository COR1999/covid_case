# Generated by Django 3.1.1 on 2020-10-07 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20201007_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='suplier_name',
            new_name='supplier_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='has_size',
        ),
    ]
