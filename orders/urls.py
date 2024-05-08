from django.urls import path
from . import views

app_name = 'orders'


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('order_create_user/', views.order_create_user, name='order_create_user'),
]