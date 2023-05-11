from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя бренда', unique=True)

    def __str__(self):
        return str(self.name)


class CarModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя модели')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'brand'],
                name='unique_car_model'
            )
        ]

    def __str__(self):
        return str(self.name)


class Condition(models.Model):
    primary_damage = models.CharField(max_length=100, verbose_name='Первичные повреждения')
    secondary_damage = models.CharField(max_length=100, verbose_name='Вторичные повреждения')
    condition = models.CharField(max_length=100, verbose_name='Состояние')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['primary_damage', 'secondary_damage', 'condition'],
                name='unique_conditions'
            )
        ]

    def __str__(self):
        return str(self.condition)


class Spec(models.Model):
    transmission = models.CharField(max_length=100, verbose_name='Коробка передач')
    drive = models.CharField(max_length=100, verbose_name='Привод')
    engine = models.CharField(max_length=100, verbose_name='Двигатель')
    fuel = models.CharField(max_length=100, verbose_name='Тип топлива')

    def __str__(self):
        return self.engine


class Information(models.Model):
    lot_number = models.CharField(max_length=100, verbose_name='Номер лота', unique=True)
    estimate_coast = models.CharField(max_length=100, verbose_name='Оценочная стоимость')
    repair_price = models.CharField(max_length=100, verbose_name='Стоимость ремонта')
    note = models.CharField(max_length=100, verbose_name='Примечание')

    def __str__(self):
        return self.lot_number


class Auction(models.Model):
    auction_name = models.CharField(max_length=100, verbose_name='Имя аукциона')
    documents = models.CharField(max_length=100, verbose_name='Документы')
    location = models.CharField(max_length=100, verbose_name='Локация')
    seller = models.CharField(max_length=100, verbose_name='Продавец')

    def __str__(self):
        return self.auction_name


class Lot(models.Model):
    year = models.CharField(max_length=100, verbose_name='Год выпуска')
    color = models.CharField(max_length=100, verbose_name='Цвет')
    mileage = models.FloatField(max_length=100, verbose_name='Пробег')
    vin = models.CharField(max_length=100, verbose_name='Вин-номер', unique=True)
    sale_date = models.CharField(max_length=100, verbose_name='Дата продажи')
    bid = models.FloatField(max_length=100, verbose_name='Ставка')
    image = models.ImageField(verbose_name='Изображение', help_text='Choose a picture.', blank=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    spec = models.ForeignKey(Spec, on_delete=models.CASCADE)
    information = models.ForeignKey(Information, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_model.name} {self.car_model.brand}'
