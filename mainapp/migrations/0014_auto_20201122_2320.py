# Generated by Django 3.1.3 on 2020-11-22 20:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20201122_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_customer', to='mainapp.Order', verbose_name='История заказов'),
        ),
        migrations.CreateModel(
            name='NewOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, verbose_name='Населённый пункт')),
                ('receive_method', models.CharField(choices=[('self', 'Курьером в удобный для вас день'), ('delivery', 'Самовывоз'), ('post', 'Почтой')], default='self', max_length=255, verbose_name='Способ получения')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('apartment_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Квартира')),
                ('porch_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Подъезд')),
                ('floor_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Этаж')),
                ('intercom', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код домофона')),
                ('full_passport_name', models.CharField(max_length=255, verbose_name='Фамилия и Имя по паспорту')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=63, verbose_name='Электронная почта')),
                ('delivery_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата доставки')),
                ('delivery_time', models.TimeField(default=django.utils.timezone.now, verbose_name='Время доставки')),
                ('payment_method', models.CharField(max_length=255, verbose_name='Способ получения')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('status', models.CharField(choices=[('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('is_ready', 'Заказ готов'), ('completed', 'Заказ выполнен')], default='new', max_length=63, verbose_name='Статус заказа')),
                ('creation_datetime', models.DateTimeField(auto_now=True, verbose_name='Дата и время создания заказа')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_order', to='mainapp.customer', verbose_name='Покупатель')),
            ],
        ),
    ]
