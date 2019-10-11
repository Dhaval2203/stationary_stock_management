# Generated by Django 2.2.2 on 2019-10-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0018_registation'),
    ]

    operations = [
        migrations.CreateModel(
            name='a_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'a_login',
            },
        ),
    ]