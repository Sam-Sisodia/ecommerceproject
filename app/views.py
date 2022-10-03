from curses.panel import bottom_panel
import email
from unicodedata import category, name
from urllib import response
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.views  import View

from . form import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as user_logout

# def home(request):
#  return render(request, 'app/home.html')

class Productview(View):
    def get(self,request):
        mobile  = Product.objects.filter(category='M')
        leptop  = Product.objects.filter(category='L')
        topwear  = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        return render(request , 'app/home.html',{'mobile':mobile,'leptop':leptop,'topwear':topwear,'bottomwear':bottomwear})



# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class product_detail(View):
    def get(self,request,pk,):
        product  = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})




 

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')



# def mobile(request):
#  return render(request, 'app/mobile.html')

class Mobilefilter(View):
    def get(self,request,data=None):
        print(data)
        if data == None:
            mobiles = Product.objects.filter(category='M')

        elif data == "Oppo" or data=="Apple":
            mobiles = Product.objects.filter(category='M').filter(brand=data)
         
        elif data  == "below":
            mobiles = Product.objects.filter(category='M').filter(selling_price__lt=15000)

        elif data  == "above":
            mobiles = Product.objects.filter(category='M').filter(selling_price__gt=15000)

        return render(request, 'app/mobile.html',{'mobile':mobiles})




# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')



def customerregistration(request):
    if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                password1 =form.cleaned_data['password1']
                user  = User.objects.create(username = name,email=email,password=password1)                 #form.cleaned_data'['name']
                user.set_password(user.password)
                user.save()
                messages.success(request,"Account Created Sucessfully")   
            else:
                form =UserRegistrationForm(request.POST)
                content = {'form':form}
               # messages.success(request,"Somethong went wrong ")   
                return render(request ,"app/customerregistration.html",content)
    else:
        form = UserRegistrationForm()
    return render(request, 'app/customerregistration.html')




def login(request):
    if  request.method == "POST":
        username = request.POST.get('name')
        print(username)
        password =request.POST.get('password')
        print(password)
        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('profile')
           # return HttpResponse("User register ")
        else:
            #return HttpResponse("User Not ragister ")
            messages.info(request ,"Incorrect Username or Password")
            return render(request, 'app/login.html')
    else:
        return render(request, 'app/login.html')




def logout(request):
    user_logout(request)
    return render(request, 'app/customerregistration.html')


def checkout(request):
 return render(request, 'app/checkout.html')
