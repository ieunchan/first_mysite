from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("coffee", views.coffee, name = "coffee"),
    path("kfood", views.Korean_food, name="koreanfood")

]