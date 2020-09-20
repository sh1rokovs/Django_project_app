from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='возраст', null=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)

    def basket_cost(self):
        return sum(item.product.price * item.quantity for item in self.user_basket.all())

    def total_quantity(self):
        return sum(item.quantity for item in self.user_basket.all())

    class Meta:
        ordering = ['-is_active', '-is_superuser', '-is_staff', 'username']
