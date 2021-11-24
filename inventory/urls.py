from django.urls import path
from . import views as mainView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dashboard/', mainView.dashBoard, name='dashboard'),
    path('profile/', mainView.userProfile, name='profile'),
    path('view_items/', mainView.view_all_items, name='view'),
    path('employee_view_items/',
         mainView.employee_item_view, name='employee_view'),
    path('sell_items/', mainView.sell_items, name='sell'),
    path('add_user/', mainView.add_user, name='users'),
]
