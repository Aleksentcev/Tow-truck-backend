# Generated by Django 4.2.7 on 2023-11-18 05:47

import core.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('delay', models.BooleanField(verbose_name='Задержка')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
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
        migrations.AddField(
            model_name='priceorder',
            name='car_type',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='towin.cartype', verbose_name='Тип авто'),
        ),
        migrations.AddField(
            model_name='priceorder',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price_orders', to='towin.order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='priceorder',
            name='tariff',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='towin.tariff', verbose_name='Тариф'),
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_price', to='towin.priceorder', verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='order',
            name='tow_truck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='towin.towtruck', verbose_name='Эвакуатор'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score', to='towin.order', verbose_name='Заказ'),
        ),
        migrations.AddConstraint(
            model_name='cartype',
            constraint=models.UniqueConstraint(fields=('car_type',), name='unique_car_type'),
        ),
        migrations.AddConstraint(
            model_name='priceorder',
            constraint=models.UniqueConstraint(fields=('order',), name='unique_order'),
        ),
        migrations.AddConstraint(
            model_name='feedback',
            constraint=models.UniqueConstraint(fields=('order',), name='unique_order_feedback'),
        ),
    ]
