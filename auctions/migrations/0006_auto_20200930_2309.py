# Generated by Django 3.1.1 on 2020-09-30 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200930_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whose_bids', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bids',
            name='bid_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='which_listing', to='auctions.listings'),
        ),
    ]