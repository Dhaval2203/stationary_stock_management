# Generated by Django 2.2.2 on 2019-08-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_stock_p_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
