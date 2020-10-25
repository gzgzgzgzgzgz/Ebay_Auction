from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"Name: {self.username} Email: {self.email} Password: {self.password}"



class Listing(models.Model):
    seller_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    title = models.CharField(max_length= 20)
    image = models.ImageField(upload_to ='static/images/')
    initial_bid = models.DecimalField(max_digits = 10, decimal_places = 2) 

class Comment(models.Model):
    text = models.CharField(max_length=100)
    user_name = models.ForeignKey(User,  on_delete=models.CASCADE, related_name="comment")
    comment_date = models.DateField()
    comment_item = models.ForeignKey(Listing,on_delete=models.CASCADE, related_name="comment_item", null = True,
    blank = True)

class Bid(models.Model):
    bid_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="which_listing")
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    time = models.TimeField
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="whose_bids", null = True,
    blank = True)

    