from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('phones/', views.phones_index, name='phones'),
    path('phones/<int:phone_id>', views.phone_detail, name="detail"),
    path('phones/create/', views.PhoneCreate.as_view(), name="phone_create"),
    path('phones/<int:pk>/update/', views.PhoneUpdate.as_view(), name="phone_update"),
    path('phones/<int:pk>/delete/', views.PhoneDelete.as_view(), name="phone_delete"),
    ]