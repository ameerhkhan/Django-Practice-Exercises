from django.db import models
from django.utils import timezone
import pandas as pd

# from django.core.signals import request_finished
# from django.dispatch import receiver

import datetime

# Create your models here.
class Fruit(models.Model):
    name_of_fruit = models.CharField(max_length=20)
    price_of_fruit = models.IntegerField(default=0)
    updated_on = models.DateTimeField('date published')

    prices = []

    def __str__(self):
        return self.name_of_fruit

    def was_updated_recently(self):
        return self.updated_on >= timezone.now() - datetime.timedelta(days=1)

    # def datas(self):
    #     self.prices.append((self.name_of_fruit, self.price_of_fruit, self.updated_on))
    #     return self.prices

    # @receiver(request_finished)
    # def data_update(sender, **kwargs):
    #     # self.prices.append((self.name_of_fruit, self.price_of_fruit, self.updated_on))
    #     # return self.prices
    #     return datas(sender)
