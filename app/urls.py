from app.models import Profile
from django.contrib import admin
from django.urls import path, include
from django.views.generic import *

from . import views
urlpatterns = [
   path('',views.Loginpage,name='loginpage'),
   path('home', views.IndexPage.as_view(),name='home'),
   path('registrationpage',views.RegistrationPage,name='registrationpage'),
   path('register',views.Registration,name='register'),
   path('login',views.Login,name='login'),
   path('shop-by-brands',views.ShopProduct,name='brands'),
   path('search',views.Search,name='search'),
   path('profile/<int:pk>',views.profile.as_view(),name="profile"),
   path('editprofile/<int:pk>',views.UpdateProfilePage,name="editprofile"),
   path('updatedprofile/<int:pk>',views.UpdateProfile,name="uprofile"),
   path("product-details/<int:pid>",views.SingleProduct,name="single"),
   path('addtocart/',views.AddtoCart,name="addcart"),
   path("showcart",views.ShowCart,name = "cart"),
   path("order-confirmation",views.Buy,name="buy"),
]