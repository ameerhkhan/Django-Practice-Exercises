# Generated by Django 3.1.1 on 2021-03-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_fruit', models.CharField(max_length=20)),
                ('price_of_fruit', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]