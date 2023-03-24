from pathlib import PurePath
from django.contrib import admin

# Register your models here.
from . models import *

@admin.register(customer)
class customerModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','locality','city','zipcode','state']


@admin.register(Product)
class prodctModelAdmin(admin.ModelAdmin):
    list_display =['title','selling_price','discount_price','discription','brand','category','product_image']




@admin.register(Cart)
class CartMOdelAdmin(admin.ModelAdmin):
    list_display =['user','product','quantity']


@admin.register(OrderPlace)
class orderplaceMOdelAdmin(admin.ModelAdmin):
    list_display = ['user','customer','product','quantity','ordered_date','status']
