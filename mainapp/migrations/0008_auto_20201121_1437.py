# Generated by Django 3.1.3 on 2020-11-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20201121_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
