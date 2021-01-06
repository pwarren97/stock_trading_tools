from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.LogIn.as_view(), name='login'),
    path('logout/', views.log_out, name='log out')
    # path('<str:user>/', views.results, name='results'),
]
