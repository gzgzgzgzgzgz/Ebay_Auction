# Generated by Django 3.1.1 on 2020-10-01 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200930_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='initial_bid',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
            preserve_default=False,
        ),
    ]
