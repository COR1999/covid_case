# Generated by Django 3.1.1 on 2020-10-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_bag', '0002_auto_20201004_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
