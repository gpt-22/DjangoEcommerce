# Generated by Django 3.1.3 on 2020-11-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20201121_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
