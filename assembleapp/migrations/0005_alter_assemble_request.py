# Generated by Django 4.1.1 on 2023-03-20 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assembleapp', '0004_remove_cabin_speciality_remove_cables_speciality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assemble',
            name='request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assembleapp.category'),
        ),
    ]
