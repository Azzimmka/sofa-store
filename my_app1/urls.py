from django.urls import path

from my_app1 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop')
]