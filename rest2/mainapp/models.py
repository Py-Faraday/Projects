from django.db import models
from django.db.models import Avg,Min,Max,Sum


class Shop(models.Model):
    name = models.CharField(max_length= 127)
    time_start = models.TimeField()
    time_end = models.TimeField()
    addres = models.CharField(max_length= 127)

    @property
    def avg_ticket_price(self):
        return self.tickets.aggregate(Avg('price'))['price_avg']

    @property
    def min_ticket_price(self):
        return self.tickets.aggregate(Max('price'))['price_min']

    @property
    def max_ticket_price(self):
        return self.tickets.aggregate(Min('price'))['price_min']
    
    @property
    def price_amount(self):
        return self.tickets.count()

    @property
    def counts_price(self):
        return self.tickets.aggregate(Sum('price'))['price__sum']

class Ticket(models.Model):
    shop = models.ForeignKey(Shop,on_delete = models.CASCADE, related_name = 'tickets')
    name = models.CharField(max_length=127)
    price = models.PositiveIntegerField(default=0)
    replace_from = models.CharField(max_length= 127)
    replace_to = models.CharField(max_length= 127)

    

    