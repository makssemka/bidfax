# Generated by Django 4.2 on 2023-05-02 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_name', models.CharField(max_length=100, verbose_name='Имя аукциона')),
                ('documents', models.CharField(max_length=100, verbose_name='Документы')),
                ('location', models.CharField(max_length=100, verbose_name='Локация')),
                ('seller', models.CharField(max_length=100, verbose_name='Продавец')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Имя бренда')),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Имя модели')),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_damage', models.CharField(max_length=100, verbose_name='Первичные повреждения')),
                ('secondary_damage', models.CharField(max_length=100, verbose_name='Вторичные повреждения')),
                ('condition', models.CharField(max_length=100, verbose_name='Состояние')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_number', models.CharField(max_length=100, unique=True, verbose_name='Номер лота')),
                ('estimate_coast', models.CharField(max_length=100, verbose_name='Оценочная стоимость')),
                ('repair_price', models.CharField(max_length=100, verbose_name='Стоимость ремонта')),
                ('note', models.CharField(max_length=100, verbose_name='Примечание')),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100, verbose_name='Цвет')),
                ('mileage', models.FloatField(max_length=100, verbose_name='Пробег')),
                ('vin', models.CharField(max_length=100, unique=True, verbose_name='Вин-номер')),
                ('sale_date', models.CharField(max_length=100, verbose_name='Дата продажи')),
                ('bid', models.FloatField(max_length=100, verbose_name='Ставка')),
                ('image', models.ImageField(blank=True, help_text='Choose a picture.', upload_to='', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transmission', models.CharField(max_length=100, verbose_name='Коробка передач')),
                ('drive', models.CharField(max_length=100, verbose_name='Привод')),
                ('engine', models.CharField(max_length=100, verbose_name='Двигатель')),
                ('fuel', models.CharField(max_length=100, verbose_name='Тип топлива')),
            ],
        ),
        migrations.AddConstraint(
            model_name='spec',
            constraint=models.UniqueConstraint(fields=('transmission', 'drive', 'fuel'), name='unique_spec'),
        ),
        migrations.AddField(
            model_name='lot',
            name='auction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.auction'),
        ),
        migrations.AddField(
            model_name='lot',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.carmodel'),
        ),
        migrations.AddField(
            model_name='lot',
            name='condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.condition'),
        ),
        migrations.AddField(
            model_name='lot',
            name='information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.information'),
        ),
        migrations.AddField(
            model_name='lot',
            name='spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.spec'),
        ),
        migrations.AddConstraint(
            model_name='condition',
            constraint=models.UniqueConstraint(fields=('primary_damage', 'secondary_damage', 'condition'), name='unique_conditions'),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.brand'),
        ),
    ]
