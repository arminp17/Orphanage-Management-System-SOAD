# Generated by Django 2.2.6 on 2019-11-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20191116_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donatemoney',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
