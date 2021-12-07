from django.urls import path
from . import views as mainView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/', mainView.registerPage, name='register'),
    path('login/', mainView.loginPage, name='login'),
    path('logout/', mainView.logoutUrl, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='accounts/forgot.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
