from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:ticker_symbol>', views.stock_info, name='stock_info'),
]
