# Generated by Django 3.2.13 on 2022-06-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220615_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='peso',
            field=models.FloatField(max_length=3),
        ),
    ]
