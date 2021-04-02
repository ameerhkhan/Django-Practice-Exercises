from .models import Fruit

import pandas as pd

from django.db.models.signals import post_save
from django.dispatch import receiver



# @receiver(post_save, sender=Fruit)
# def data_collection(sender, instance, created, **kwargs):
#     # instance --> The data that has been changed.
#     # created --> Boolean.


historical = []


def data_aggregation(name, price, date):
    historical.append((name, price, date))
    return historical


