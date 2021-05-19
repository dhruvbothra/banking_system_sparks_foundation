from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home ,name="home"),
    path("customer/", views.customer ,name="customer"),
    path("<int:id>/transfer/", views.transfer ,name="transfer"),
    path("<int:id>/transfer_processing/", views.transfer_processing ,name="transfer_processing"),
    path("history/", views.history ,name="history"),
]
