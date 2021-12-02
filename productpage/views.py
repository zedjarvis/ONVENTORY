from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Contact
from django.views.generic import View
from django.http import JsonResponse


############################################################
# Main Website Page
############################################################
def homePage(request):
    return render(request, 'productpage/index.html')


# Contact Form ajax call
class ContactForm(View):
    def post(self, request):
        full_name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        email = request.POST.get('email', None)
        message = request.POST.get('message', None)

        contact = Contact(full_name=full_name,
                          email=email,
                          phone=phone,
                          message=message)
        contact.save()

        return JsonResponse({'msg': 'successful'})


# CUSTOM ERROR PAGES
def handler400(request, exception=None):
    response = render(request, "productpage/error/400.html", {})
    return response


def handler403(request, exception=None):
    response = render(request, "productpage/error/403.html", {})
    return response


def handler404(request, exception=None):
    response = render(request, "productpage/error/404.html", {})
    return response


def handler500(request, exeption=None):
    response = render(request, "productpage/error/500.html", {})
    return response
