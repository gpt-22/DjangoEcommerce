# Generated by Django 3.1.3 on 2020-11-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20201120_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='price',
            field=models.CharField(max_length=9, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='price',
            field=models.CharField(max_length=9, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='ram',
            field=models.CharField(choices=[('2 ГБ', '2 ГБ'), ('3 ГБ', '3 ГБ'), ('4 ГБ', '4 ГБ'), ('6 ГБ', '6 ГБ'), ('8 ГБ', '8 ГБ'), ('16 ГБ', '16 ГБ'), ('32 ГБ', '32 ГБ')], max_length=255, verbose_name='Объём оперативной памяти'),
        ),
    ]
