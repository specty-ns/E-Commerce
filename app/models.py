from typing import Counter
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings    
# Create your models here.
Category=(
    ('Shoes','Shoes'),
    ('Top Wear','Top Wear'),
    ('Bottom Wear','Bottom Wear'),
)
Gender=(
    ('Male','Male'),
    ('Female','Female'),
    ('Unisex','Unisex'),
)

    
    
class Profile(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(null=True)
    alt_phone_number = models.BigIntegerField(null=True)
    address_line1 = models.TextField(max_length= 100,null=True)
    address_line2 = models.TextField(max_length=100,null=True)
    city= models.CharField(max_length=50,null=True)
    state= models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50,null=True)
    zipcode = models.BigIntegerField(null=True)



class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_quantity=models.BigIntegerField()
    product_price = models.BigIntegerField()
    product_image=models.ImageField(upload_to="product_image/")
    product_brand = models.CharField(max_length=50, default='')
    product_category = models.CharField(max_length=50,choices=Category, default='')
    wear_by= models.CharField(max_length=10,choices=Gender,default='Unisex')
    product_description = models.TextField(max_length=1000, default='')

class Cart(models.Model):
    profile_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    cart_price=models.BigIntegerField(default=0)
    cart_quantity=models.BigIntegerField(default=1) 
    cart_date=models.DateTimeField(auto_now_add=True)
    cart_subtotal=models.BigIntegerField(default=0)
    
    order_status = models.CharField(max_length=50,default="Order Confirmation Pending")

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    


