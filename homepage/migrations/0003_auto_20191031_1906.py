# Generated by Django 2.1.7 on 2019-10-31 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_orphanage_orphanage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addorphan',
            name='orphanage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homepage.Orphanage'),
        ),
        migrations.AlterField(
            model_name='addorphan',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='donation',
            name='orphanage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Orphanage'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='emergency',
            name='orphanage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Orphanage'),
        ),
        migrations.AlterField(
            model_name='moneydonation',
            name='orphanage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homepage.Orphanage'),
        ),
        migrations.AlterField(
            model_name='moneydonation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transport',
            name='danation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Donation'),
        ),
    ]
