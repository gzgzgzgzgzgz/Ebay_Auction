# Generated by Django 3.1.1 on 2020-10-01 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_listings_initial_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='title',
            field=models.CharField(default='rtemo', max_length=20),
            preserve_default=False,
        ),
    ]