from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # path('<str:user>/', views.results, name='results'),
]
