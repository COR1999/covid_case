# Generated by Django 3.1.1 on 2020-10-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20201007_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(default='', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
