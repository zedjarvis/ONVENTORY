from django.urls import path
from . import views as mainView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/', mainView.registerPage, name='register'),
    path('login/', mainView.loginPage, name='login'),
    path('logout/', mainView.logoutUrl, name='logout'),
    path('forgot_password/', mainView.forgortPassword, name='forgot'),
    path('reset_password/', mainView.resetPassword, name='reset'),
]
