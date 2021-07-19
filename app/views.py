from django.conf.urls import url
from django.http import request,HttpResponse
from app.models import *
from django.contrib.auth import models
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import *
from django.views.generic import *
from django.db.models import *
from django.urls import reverse_lazy
from .task import *
from django.core.mail import send_mail

class IndexPage(TemplateView):
    template_name = "app/index.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        products = Products.objects.all().order_by('-product_quantity')[:20]
        context = {'products':products}
        return context
        

# def IndexPage(request):
#     if 'username' in request.session:
#         return render(request,"app/index.html")
#     else:
#         return redirect('loginpage')

def RegistrationPage(request):
    return render(request,'app/registration.html')
def Loginpage(request):
    return render(request,'app/login.html')

def Registration(request):
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['pass']
    cpassword=request.POST['cpass']
    firstname=request.POST['fname']
    lastname=request.POST['lname']
    if User.objects.filter(username=username):
        message="User already registered"
        return render(request,'app/registration.html',{'msg':message})
    else:
        if password==cpassword:
            newUser= User.objects.create(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
            newProfile = Profile.objects.create(user_id=newUser)
            
            return render(request,'app/login.html')
        else:
            message="password doesn't match"
            return render(request,'app/registration.html',{'msg':message})  

def Login(request):
    username=request.POST['username']
    password=request.POST['pass']
    data = User.objects.get(username=username) 
    if data and data.password==password:
        request.session['username']=data.username
        request.session['firstname']=data.first_name
        request.session['lastname']=data.last_name
        request.session['email']=data.email
        request.session['id']=data.id
        return redirect('home')
    else:
        message="username or password doesn't match"
        return render(request,'app/login.html',{'msg':message}) 

def ShopProduct(request):
    if 'username' in request.session:
        products=Products.objects.all()
        brands = products.values('product_brand').annotate(name_count=Count('product_brand')).filter(name_count__gt=0)
        category = products.values('product_category').annotate(name_count=Count('product_category')).filter(name_count__gt=0)
        sort = request.GET.get('sort')
        
        if sort !="" and sort is not None:
            if sort=="A-Z":
                products=products.order_by('product_name')
            elif sort=='Z-A':
                products=products.order_by('-product_name')
            elif sort=='L-H':
                products=products.order_by('product_price')
            elif sort=="H-L":
                products=products.order_by('-product_price')
    
        return render(request,'app/brands.html',{'products':products,'brandname':brands,'categories':category}) 
    else:
        return redirect('loginpage')

def SingleProduct(request,pid):

    if 'username' in request.session:
        single = Products.objects.get(id=pid)
        similar = Products.objects.all().filter(product_category=single.product_category)
        return render (request,"app/single-product.html",{'single':single,"similar":similar})
    else:
        return redirect('loginpage')


def Search(request):
    if 'username' in request.session:
        template_name="app/brands.html"
        model= Products.objects.all()
        brandname = model.values('product_brand').annotate(name_count=Count('product_brand')).filter(name_count__gt=0)
        categories = model.values('product_category').annotate(name_count=Count('product_category')).filter(name_count__gt=0)
        
        query = request.GET.get('q')
        if query!= "" and query is not None:
            model = model.filter(product_name__icontains=query) | model.filter(product_category__icontains=query)
            
        return render(request, template_name, {'object_list':model,'brandname':brandname,'categories':categories})
    else:
        return redirect('loginpage')

class profile(TemplateView):    
    template_name = "app/profile.html"    
    def get_context_data(request,pk, **kwargs):        
            context=super().get_context_data(**kwargs)
            user = Profile.objects.get(user_id__id=pk)
            context = {'user':user}
            return context


def UpdateProfilePage(request,pk):
    if 'username' in request.session:
        profiledata = Profile.objects.get(user_id__id=pk)
        return render(request,'app/edit_profile.html',{'profile':profiledata})
    else:
        return redirect('loginpage')

def UpdateProfile(request,pk):
    if 'username' in request.session:        
        udata = Profile.objects.get(user_id__id=pk)

        udata.user_id.first_name = request.POST['fname']
        udata.user_id.last_name = request.POST['lname']
        udata.phone_number = request.POST['mob']
        udata.alt_phone_number = request.POST['altmob']
        udata.address_line1 = request.POST['line1']
        udata.address_line2 = request.POST['line2']
        udata.city= request.POST['city']
        udata.state= request.POST['state']
        udata.country = request.POST['country']
        udata.zipcode = request.POST['zip']
        udata.save()
        url = f'/profile/{pk}'
        return redirect(url)
    else:
        return redirect('loginpage')
    

    
def AddtoCart(request):
    if 'username' in request.session:   
        user= Profile.objects.get(user_id__id=request.session['id'])
        pro_id = request.GET['pid']
        pro = Products.objects.get(id=pro_id)
        qty = 1
        cart_sub = pro.product_price * qty
        tax =  cart_sub * 0.18
        grand = cart_sub + tax
        
        print("YOooooooooooooooooooo33")
        newCart = Cart(profile_id=user, product_id = pro, cart_price = pro.product_price, cart_quantity = 1, cart_subtotal = cart_sub)
        newCart.save()

        return HttpResponse('Item added to your card')
    # {{ value|floatformat:2 }}
    else:
        return redirect('loginpage')

def ShowCart(request):
    if 'username' in request.session:     
        print(request.session['id'])
        cartdata = Cart.objects.all().filter(profile_id__user_id=request.session['id'],order_status="Order Confirmation Pending")
        subtotal = 0
        tax  = 0
        grand = 0
        for t in cartdata:
            subtotal += t.cart_subtotal
            tax  = subtotal * 0.18
            grand = subtotal + tax
        return render (request,"app/cart.html",{'cartdata':cartdata,'subtotal':subtotal,'total':grand,"tax":tax})
    else:
        return redirect('loginpage')

def Buy(request):
    if 'username' in request.session: 
        # for c in request.POST['cid']:
        #     print(request.POST['cid'])
        # d = Cart.objects.all().filter(profile_id__user_id=request.session['id']).exclude(order_status="Order Confirmation Pending")
        pro = Products.objects.get(id=request.POST['pid'])
        for data in Cart.objects.all().filter(profile_id__id=request.POST['cid'],order_status="Order Confirmation Pending"):

            if  pro.product_quantity >= data.cart_quantity:
                pro.product_quantity -= data.cart_quantity
                data.order_status = "Order Accepted"
                pro.save()
                data.save()
                send_mail_accept.delay()

            else:
                data.order_status = "Order Rejected"
                data.save()
                send_mail_reject.delay()               
       
        return render(request,"app/confirmation.html")
    else:
        return redirect('loginpage') 
