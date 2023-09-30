from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_data", views.get_latest_data),
    path("get_latest_exchange_data", views.get_latest_exchange_rate),
    path("get_all_data", views.get_all_data)
]