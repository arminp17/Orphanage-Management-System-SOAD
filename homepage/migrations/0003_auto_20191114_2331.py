# Generated by Django 2.2.5 on 2019-11-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20191114_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='status',
            field=models.CharField(default='Freshly Applied', max_length=50),
        ),
    ]
