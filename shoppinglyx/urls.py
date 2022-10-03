from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('reset_password/',auth_view.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/',auth_view.PasswordResetDoneView.as_view(), name="reset_password_Done"),
    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(), name = "reset_password_confirm"),
    path('reset_password_complete/',auth_view.PasswordResetCompleteView.as_view(), name = "reset_password_complete")
]
