from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page),
    path('places/<int:pk>', views.only_one_place_information)
]