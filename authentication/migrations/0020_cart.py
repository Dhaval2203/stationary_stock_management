# Generated by Django 2.2.2 on 2019-10-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0019_a_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=50)),
                ('p_category', models.CharField(max_length=50)),
                ('p_company', models.CharField(max_length=50)),
                ('p_img', models.ImageField(upload_to='')),
                ('stock', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
