from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Имя категории', max_length=128)
    description = models.TextField(verbose_name='Описание категории', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    class Meta:
        ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория продукта')
    name = models.CharField(verbose_name='Имя продукта', max_length=128)
    image = models.ImageField(upload_to='Products_image', blank=True)
    short_desc = models.CharField(verbose_name='Краткое описание продукта', max_length=64, blank=True)
    description = models.TextField(verbose_name='Описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    @classmethod
    def get_items(cls):
        return cls.objects.filter(is_active=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
