from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Имя категории', max_length=128)
    description = models.TextField(verbose_name='Описание категории', blank=True)


def __str__(self):
    return f'{self.__class__.__name__}: {self.name}'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория продукта')
    name = models.CharField(verbose_name='Имя продукта', max_length=128)
    image = models.ImageField(upload_to='Products_image', blank=True)
    short_desc = models.CharField(verbose_name='Краткое описание продукта', max_length=64, blank=True)
    description = models.TextField(verbose_name='Описание продукта', blank=True)
    price = models.DecimalField(verbose_name='Цена продукта', max_digits=8, decimal_place=2, default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
