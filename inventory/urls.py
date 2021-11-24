from django.urls import path
from . import views as mainView
from productpage import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dashboard/', views.handler404, name='dashboard'),
    path('profile/', mainView.userProfile, name='profile'),
    path('view_items/', mainView.view_all_items, name='view'),
    path('employee_view_items/',
         mainView.employee_item_view, name='employee_view'),
    path('sell_items/', views.handler404, name='sell'),
    path('add_user/', mainView.add_user, name='users'),
]
