from django.urls import path
from . import views as mainView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', mainView.homePage, name='productpage'),
    path('contact/', mainView.ContactForm.as_view(), name='contact'),
]
