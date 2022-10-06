from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/',include('API.urls'))
   # path('auth', include('django.contrib.auth.urls'))
    # path('password_change/ ',auth_views.PasswordChangeView.as_view(),  name="reset_password"),
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(), name="reset_password_Done"),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm'"),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(), name = "reset_password_complete")
]



# login/ [name='login']
# logout/ [name='logout']
# password_change/ [name='password_change']
# password_change/done/ [name='password_change_done']
# password_reset/ [name='password_reset']
# password_reset/done/ [name='password_reset_done']
# reset/<uidb64>/<token>/ [name='password_reset_confirm']
# reset/done/ [name='password_reset_complete']


#  path('',auth_views.PasswordResetView.as_view(),  name="reset_password"),
#     path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="reset_password_Done"),
#     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name = "reset_password_confirm"),
#     path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name = "reset_password_complete")



#https://ordinarycoders.com/blog/article/django-password-reset