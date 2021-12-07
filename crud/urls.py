from django.urls import path
from . import views as mainView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('create_user/', mainView.CreateUser.as_view(), name='create_user'),
    path('create_category/', mainView.CreateCategory.as_view(),
         name='create_category'),
    path('create_shop/', mainView.CreateShop.as_view(), name='create_shop'),
    path('create_item/', mainView.CreateItem.as_view(), name='create_item'),
    path('delete_employee/<int:id>/',
         mainView.delete_employee, name='delete_employee'),
    path('delete_item/<int:id>/', mainView.delete_item, name='delete_item'),
    path('edit_item/<int:id>/', mainView.EditItem.as_view(), name='edit_item'),
    path('export/items_to_csv/', mainView.export_items_csv, name='to_csv'),
    path('export/items_to_xls/', mainView.export_items_xls, name='to_xls'),
    path('export/items_to_pdf/', mainView.export_items_pdf, name='to_pdf'),
]
