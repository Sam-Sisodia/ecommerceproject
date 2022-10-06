from xml.dom.minidom import Document
from django.urls import path
from app import views
from django.conf  import settings
from django.conf.urls.static  import static




urlpatterns = [
    #path('', views.home),
    path('',views.Productview.as_view()),
    path('product-detail/<int:pk>',views.product_detail.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profileview.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.Mobilefilter.as_view(), name='mobile'),
    path('mobile/<slug:data>', views.Mobilefilter.as_view(), name='mobile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.customerregistration, name='customerregistration'),

   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)






















































































'''
 path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),

'''