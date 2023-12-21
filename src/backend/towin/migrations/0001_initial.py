# Generated by Django 4.2.7 on 2023-12-21 22:11

import core.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('comment', models.CharField(blank=True, max_length=400, null=True, verbose_name='Комментарий')),
                ('ontime', models.BooleanField(default=True, verbose_name='Водитель приехал вовремя')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('-pub_date',),
                'default_related_name': 'feedbacks',
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
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Созданный', 'Созданный'), ('Активный', 'Активный'), ('Завершенный', 'Завершенный'), ('Отмененный', 'Отмененный')], default='Созданный', verbose_name='Статус заказа')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата заказа')),
                ('delivery_time', models.DateTimeField(default=django.utils.timezone.now, help_text='В случае если заказ "Отложенный", укажите здесь дату и время подачи.', verbose_name='Время подачи')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
                'default_related_name': 'orders',
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
                'default_related_name': 'price_orders',
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Эконом', 'Эконом'), ('Экспресс', 'Экспресс'), ('Манипулятор', 'Манипулятор')], max_length=50, verbose_name='Название тарифа')),
                ('description', models.CharField(max_length=255, verbose_name='Описание тарифа')),
                ('price', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Цена тарифа')),
                ('delivery_time', models.TimeField(null=True, verbose_name='Время подачи')),
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
                ('license_plates', models.CharField(max_length=12, validators=[core.validators.plate_validator], verbose_name='Гос. номер')),
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
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='towin.order', verbose_name='Заказ'),
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
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='towin.priceorder', verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='order',
            name='tow_truck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='towin.towtruck', verbose_name='Эвакуатор'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='towin.order', verbose_name='Заказ'),
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
