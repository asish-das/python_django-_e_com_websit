# Generated by Django 4.1.1 on 2023-03-20 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assembleapp', '0003_cabin_image_cables_image_display_image_hdd_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabin',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='cables',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='display',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='hdd',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='keyboard',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='motherboard',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='mouse',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='product',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='ram',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='smps',
            name='speciality',
        ),
    ]
