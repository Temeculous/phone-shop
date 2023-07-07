from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('phones/', views.phones_index, name='phones'),
    ]