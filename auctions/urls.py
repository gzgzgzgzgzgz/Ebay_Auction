from django.urls import path

from . import views
app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing/<str:username>", views.create_listing, name = "create_listing"),
    path("added_listing/<str:username>", views.added_listing, name = "added_listing")
    ]
