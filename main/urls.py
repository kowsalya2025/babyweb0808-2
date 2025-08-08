from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/pampers/', views.pampers_view, name='products_pampers'),
    path('products/boys/', views.boys_view, name='products_boys'),
    path('products/girls/', views.girls_view, name='products_girls'),
    path('products/soap/', views.soap_view, name='products_soap'),
    path('products/stroller/', views.stroller_view, name='products_stroller'),
    path('products/bottle/', views.bottle_view, name='products_bottle'),
    path('offers/', views.offers_view, name='offers'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('cart/', views.cart_view, name='cart'),
    path('login/', views.login_view, name='login'),
    
]
