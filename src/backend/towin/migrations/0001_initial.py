# Generated by Django 4.2.7 on 2023-11-23 11:11

import core.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('Легковой', 'Легковой'), ('Грузовой', 'Грузовой'), ('Мотоцикл', 'Мотоцикл'), ('Спецтехника', 'Спецтехника')], verbose_name='Тип машины')),
                ('price', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Цена за тип авто')),
            ],
            options={
                'verbose_name': 'Тип авто',
                'verbose_name_plural': 'Типы авто',
                'default_related_name': 'car_type',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('comment', models.CharField(blank=True, max_length=400, null=True, verbose_name='Комментарий')),
                ('ontime', models.BooleanField(verbose_name='Водитель приехал вовремя')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_from', models.CharField(max_length=200, verbose_name='Адрес подачи')),
                ('address_to', models.CharField(max_length=200, verbose_name='Адрес прибытия')),
                ('addition', models.CharField(blank=True, max_length=300, null=True, verbose_name='Комментарий')),
                ('delay', models.BooleanField(default=False, verbose_name='Задержка')),
                ('order_date', models.DateTimeField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-order_date',),
            },
        ),
        migrations.CreateModel(
            name='PriceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wheel_lock', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='Заблокированные колеса')),
                ('towin', models.BooleanField(verbose_name='Кюветные работы')),
                ('total', models.PositiveSmallIntegerField(default=0, verbose_name='Итоговая цена')),
            ],
            options={
                'verbose_name': 'Заказы и Цены',
                'verbose_name_plural': 'Заказы и цены',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Фамилия')),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Эконом', 'Эконом'), ('Экспресс', 'Экспресс'), ('Манипулятор', 'Манипулятор')], max_length=50, verbose_name='Название тарифа')),
                ('description', models.CharField(max_length=255, verbose_name='Описание тарифа')),
                ('price', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Цена тарифа')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='TowTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(verbose_name='Статус эвакуатора.')),
                ('driver', models.CharField(help_text='Укажите водителя', max_length=255, verbose_name='Водитель')),
                ('model_car', models.CharField(max_length=255, verbose_name='Модель и марка эвакуатора')),
                ('license_plates', models.CharField(max_length=10, validators=[core.validators.plate_validator], verbose_name='Гос. номер')),
            ],
            options={
                'verbose_name': 'Эвакуатор',
                'verbose_name_plural': 'Эвакуаторы',
            },
        ),
        migrations.AddConstraint(
            model_name='towtruck',
            constraint=models.UniqueConstraint(fields=('driver',), name='unique_driver'),
        ),
        migrations.AddConstraint(
            model_name='tariff',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_tariff_name'),
        ),
    ]
