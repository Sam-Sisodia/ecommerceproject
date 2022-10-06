from API import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('', views.home),
    path('',views.Productviews.as_view()),
    path('<slug:data>',views.Productviews.as_view()),
]