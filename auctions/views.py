from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from auctions.models import Listing, User, Bid, Comment
from django import forms

from .models import User

class NewListing(forms.Form):
    pass

def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request,username):
    return render(request, "auctions/create_listing.html", {
        "username" : username
    })

def added_listing(request,username):
    if request.method == "POST":
        newlist = NewListing(request.POST)
        if newlist.is_valid():
            title = request.POST.get('title')
            description = request.POST.get('description')
            img = request.POST.get('image')
            bid = request.POST.get('bid')
            #Listings.objects.create(seller_name = username, )
            user = User.objects.get(username = username)
            new_listing = Listing(seller_name = user, description = description, 
            title = title, initial_bid = bid, image = img)
            new_listing.save()
            return HttpResponseRedirect(reverse("auctions:index"))



