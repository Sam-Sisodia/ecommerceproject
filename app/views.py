
import imp
from itertools import product
import re
from statistics import quantiles
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.views  import View

from . form import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as user_logout
from django.db.models import Q
from django.http import JsonResponse


''' user permission urls after login '''


from django.contrib.auth.decorators import login_required #functionbased view 
from django.utils.decorators import  method_decorator     #classbased
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
        item_already_in_cart= False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})




 



def buy_now(request):
 return render(request, 'app/buynow.html')



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



@login_required(login_url='/login/')
def logout(request):
    user_logout(request)
    return redirect('login')

from django.contrib.auth.mixins import LoginRequiredMixin
class profileview(LoginRequiredMixin,View):
    login_url = '/login/'
        
    def get(self,request):
        form = CustomerProfileform()
        return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})  
    def post(self,request):
        form = CustomerProfileform(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            user = customer(user = usr ,name=name ,locality= locality,city=city,zipcode=zipcode,state=state)
            user.save()
            messages.success(request,"Profile Update Sucessfully ")   
        return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})  

def address(request):
    address = customer.objects.filter(user = request.user)
    return render(request, 'app/address.html',{'address':address,'active':'btn-primary'})


@login_required(login_url='/login/')
def add_to_cart(request):
    user = request.user  
    print(user)
    product_id = request.GET.get('prod_id')
    print(product_id)
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    #return render(request, 'app/addtocart.html')
    return redirect('/cart')


'''
SHOW  CART  VIEW WITHOUT  PAYMENT 

def show_cart(request):
    user  = request.user
    cart = Cart.objects.filter(user=user)
    return render(request, 'app/addtocart.html',{'carts':cart})

'''

@login_required(login_url='/login/')
def show_cart(request):
    if request.user.is_authenticated:
        user  = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0.0
        shipping_amount= 70.0
        total_amount = 0.0
        cart_product =  [ p for p in Cart.objects.all() if p.user == user]

        if cart_product: 
            for p in cart_product:
                tempamount = (p.quantity * p.product.selling_price)
                amount = amount +tempamount
                total_amount =  amount +shipping_amount

        return render(request, 'app/addtocart.html',{'carts':cart , 'amount':amount,'total_amount':total_amount})

@login_required(login_url='/login/')
def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount= 70.0
        cart_product =  [ p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount = amount +tempamount
            total_amount =  amount +shipping_amount
        data = {
            'quantity':c.quantity,
            'amount'  : amount,
            'total_amount': total_amount
            }
        return JsonResponse(data)
@login_required(login_url='/login/')
def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount= 70.0
        cart_product =  [ p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount = amount +tempamount
            #total_amount =  amount +shipping_amount
        data = {
            'quantity':c.quantity,
            'amount'  : amount,
            'total_amount':amount+  shipping_amount
            }
        return JsonResponse(data)




@login_required(login_url='/login/')
def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount= 70.0
        cart_product =  [ p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount = amount +tempamount
            #total_amount =  amount +shipping_amount
        data = {
           # 'quantity':c.quantity,
            'amount'  : amount,
            'total_amount' : amount+ shipping_amount
            }
        return JsonResponse(data)



@login_required(login_url='/login/')
def checkout(request):
  user = request.user
  currentuser = customer.objects.filter(user=user)
  cart_items = Cart.objects.filter(user=user)
  amount = 0.0
  shipping_amount= 70.0
  total_amount = 0.0
  cart_product =  [ p for p in Cart.objects.all() if p.user == user]
  if cart_product: 
    for p in cart_product:
        tempamount = (p.quantity * p.product.selling_price)
        amount = amount +tempamount
    total_amount =  amount +shipping_amount

  return render(request, 'app/checkout.html',{'total_amount': total_amount,'currentuser':currentuser,'cart_items':cart_items})



@login_required(login_url='/login/')
def paymentdone(request):
    user = request.user
    print(user)
    custid = request.GET.get('custid')
    print(custid)
    cutomers = customer.objects.get(id=custid)
    cart= Cart.objects.filter(user=user)
    for c in cart:
        OrderPlace(user=user, customer=cutomers, product= c.product, quantity= c.quantity).save()
        c.delete()

    return redirect("orders")


@login_required(login_url='/login/')
def orders(request):
    order_placed = OrderPlace.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed':order_placed})

























































































# sudo  /opt/lampp/./manager-linux-x64.run




'''
 <hr>
    <form action="">
      {% for user in  currentuser %}
      <div class="card">
        <div class="card-body">
        <h5>{{user.name}}</h5>
        <p>{{user.locality}},{{user.city}},{{user.zipcode}}, {{user.state}}</p>
        </div>
      </div>
        <div class="form-check mt-2 mb-5">
          <input class="form-check-input" type="radio" value="">
          <label class="form-check-label fw-bold" for="">
            Address: {{forloop.counter}}</label>
        </div>
        {{endfor}}
        <div class="text-end">


'''