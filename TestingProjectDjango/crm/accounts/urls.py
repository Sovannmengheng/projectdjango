from django.urls import path
from . import views

urlpatterns = [
    path('', views.ogani),
    path('shopdetails/', views.shopdetails, name='shopdetails'),
    path('shopingCart/', views.shopingCart, name='shopingCart'),
    path('checkout/', views.checkout, name='checkout'),
    path('shopgrid/', views.shopgrid, name='shopgrid'),
    path('Blog/', views.Blog, name='Blog'),
    path('BlogDetails/', views.BlogDetails, name='BlogDetails'),

    path('products/', views.products),
    path('customer/', views.customer),
    path('viewmengheng/', views.mengheng),
    path('ViewIndex/', views.ViewIndex),
    path('AboutUs/', views.Aboutus),
    path('ViewIndex/<int:CustomerID>/', views.ViewIndex),
    path('index/', views.index),
    path('MenuDetailMethod/<int:pk>/', views.MenuDetailMethod , name="MenuDetailMethod"),
]