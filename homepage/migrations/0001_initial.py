# Generated by Django 2.1.2 on 2019-11-10 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import homepage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOrphan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('find_place', models.CharField(max_length=100)),
                ('ref_no', models.IntegerField()),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_donation', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField()),
                ('donation_type', models.CharField(choices=[('F', 'Food'), ('C', 'Clothes'), ('B', 'Book'), ('E', 'Eletrical Appliances'), ('O', 'other')], max_length=1)),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(max_length=100)),
                ('situation', models.CharField(max_length=500)),
                ('date_of_post', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_event', models.CharField(max_length=50)),
                ('date_of_post', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('event', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyDonation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_donation', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orphan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orphan_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('special_skills', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Orphanage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orphanage_name', models.CharField(max_length=30)),
                ('year_of_establishment', models.IntegerField()),
                ('lon', models.FloatField(null=True)),
                ('lat', models.FloatField(null=True)),
                ('address', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=homepage.models.image_upload_url)),
                ('description', models.CharField(max_length=300)),
                ('orphanage_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('danation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Donation')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_no', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone_no', models.IntegerField()),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='orphan',
            name='orphanage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Orphanage'),
        ),
        migrations.AddField(
            model_name='moneydonation',
            name='orphanage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homepage.Orphanage'),
        ),
        migrations.AddField(
            model_name='moneydonation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='events',
            name='orphanage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homepage.Orphanage'),
        ),
        migrations.AddField(
            model_name='events',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='emergency',
            name='orphanage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Orphanage'),
        ),
        migrations.AddField(
            model_name='donation',
            name='orphanage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Orphanage'),
        ),
        migrations.AddField(
            model_name='donation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addorphan',
            name='orphanage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homepage.Orphanage'),
        ),
        migrations.AddField(
            model_name='addorphan',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
