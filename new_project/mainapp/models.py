from django.db import models



class Product(models.Model):
    name = models.CharField(max_length= 127 )
    description = models.TextField()
    price = models.IntegerField()
    articul = models.CharField(max_length = 127)


class Cart(models.Model):
    user_name = models.CharField(max_length = 127, verbose_name = 'Имя')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')
    total_price = models.IntegerField(verbose_name = ' Баланс в Карте')
    delivery_address = models.CharField(max_length = 127, verbose_name = 'Адрес')


class CartProduct(models.Model):
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart , on_delete = models.CASCADE)
    total_price = models.IntegerField()
    amount = models.IntegerField()