# Generated by Django 4.1.1 on 2023-03-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assembleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pin',
            field=models.IntegerField(),
        ),
    ]
