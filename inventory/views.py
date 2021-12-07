# -*- encoding: utf-8 -*-


from django.shortcuts import redirect, render
from .models import Shop
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Dashboard View
@staff_member_required(login_url="login")
def dashBoard(request):
    if request.user.is_employed:
        return redirect('employee_view')

    return render(request, 'inventory/dashboard.html', {})


# User profile view
@login_required(login_url="login")
def userProfile(request):
    return render(request, 'inventory/profile.html', {})


# employee item view
@login_required(login_url="login")
def employee_item_view(request):
    items = request.user.employee_set.get().shop.items.all()
    categories = request.user.employee_set.get().shop.categories.all()

    context = {'items': items,
               'categories': categories}

    return render(request, 'inventory/view_item.html', context)


# employer viewing items per shop
@staff_member_required(login_url="login")
def view_items_per_shop(request, shop):
    # allowed only for shop owners
    if request.user.is_employed:
        return redirect('employee_view')

    shop = Shop.objects.get(owner=request.user, shop_name=shop)
    items = shop.items.all()
    categories = shop.categories.all()

    context = {'items': items,
               'categories': categories}

    return render(request, 'inventory/view_item.html', context)


# employer viewing all items
@staff_member_required(login_url="login")
def view_all_items(request):
    if request.user.is_employed:
        return redirect('employee_view')

    items_object_list = []
    category_list = []
    shops = request.user.shops.all()
    for shop in shops:
        items_object_list += shop.items.all()
        category_list += shop.categories.all()

    return render(request, 'inventory/view_item.html',
                  {'items': items_object_list, 'shops': shops,
                   'categories': category_list})


# Sell Items View
def sell_items(request):
    return render(request, 'inventory/sell_item.html', {})


# Adding User view
@staff_member_required(login_url="login")
def add_user(request):
    users = request.user.employees.all()
    shops = request.user.shops.all()
    context = {'users': users,
               'shops': shops}

    return render(request, 'inventory/add_user.html', context)


# notifications page
def notification_view(request):
    return render(request, 'inventory/notifications.html', {})


# settings page
def settings_view(request):
    return render(request, 'inventory/settings.html', {})
