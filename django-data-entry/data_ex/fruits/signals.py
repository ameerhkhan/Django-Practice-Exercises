from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Fruit
from django.utils import timezone
import pandas as pd
import datetime

historical = []
# historical_prices = pd.DataFrame()
hist_dict = {
    'DATE': [''],
    'NAME': '',
    'PRICE': ''
}
# historical_prices = pd.DataFrame(hist_dict).set_index('DATE')
name_fruit = []
price_fruit = []
updating = []
# df3 = pd.DataFrame()

# index is going to be the timezone attribute in the created dataframe.
# df = pd.DataFrame.from_dict(df, orient='index').fillna('').astype(int,raise_on_error=False)


@receiver(post_save, sender=Fruit)
def updating(sender, instance, created, **kwargs):
    # historical_prices2 = pd.DataFrame(hist_dict).set_index('DATE').fillna('')
    historical.append((instance.name_of_fruit, instance.price_of_fruit, instance.updated_on))
    hist_dict['DATE'] = [instance.updated_on.strftime("%x")]
    hist_dict['NAME'] = instance.name_of_fruit
    hist_dict['PRICE'] = instance.price_of_fruit
   
   

    print(hist_dict)

    # Now add this dictionary to the dataframe.
    df = pd.DataFrame(hist_dict).set_index('DATE')
    # df2 = pd.Series(hist_dict, name='DATE')
    # historical_prices2.update(df)
    # historical_prices2.append(df2)
    # df3.update(df)
    # pd.merge(historical_prices, df, how='left', left_index=True, right_index=True)
    Fruit.updated_on = timezone.now()
    print(Fruit.updated_on)

    # and now convert it to csv
    # print(historical_prices)
    # print(historical_prices2)
    print(df)
    # historical_prices2.to_csv("historical.csv")

    # DATE CONVENTION --> MONTH, DAY, YEAR
    df.to_csv('fruits/assets/historical.csv', mode='a', header=False)
    # Create a new csv file with the headers already inplace for effective use. header = False will remove
    # HEADINGS i.e. DATE, NAME, PRICE
    backup_file = open('fruits/assets/backup.txt', "a")
    backup_file.write("\n" + str(historical[0]))
    backup_file.close()

    # add this into a pandas dataframe instead of a list.
    # print(historical)
    # return(historical)
