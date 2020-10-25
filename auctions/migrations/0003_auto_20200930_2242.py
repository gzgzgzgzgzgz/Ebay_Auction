# Generated by Django 3.1.1 on 2020-09-30 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bids_comments_listings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.comments'),
        ),
    ]
