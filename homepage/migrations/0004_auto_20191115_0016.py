# Generated by Django 2.2.5 on 2019-11-14 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20191114_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='orphanage',
            name='status',
            field=models.CharField(default='Freshly Applied', max_length=50),
        ),
        migrations.AlterField(
            model_name='events',
            name='date_of_post',
            field=models.DateField(default=datetime.date(2019, 11, 15)),
        ),
    ]
