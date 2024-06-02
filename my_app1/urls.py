from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('contacts/', views.contact, name='contacts'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact_view, name='contact'),
]