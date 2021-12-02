from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic import View
from django.http import JsonResponse
from inventory.models import Employee, Item, Shop, Category
from accounts.models import User
import random


# create user ajax view
class CreateUser(View):
    def post(self, request):
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)
        shop_name = request.POST.get('shop', None)
        salt = ["1234", "4567", "548", "987", "3748",
                '2734', "2234", "456", "567", "965"]
        username = first_name + last_name + random.choice(salt)
        password = 'User1234'
        shop = request.user.shops.get(shop_name=shop_name)

        user = User.objects.create_user(email, username, password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = False
        user.is_employed = True
        user.save()

        employee = Employee(user=user, shop=shop, employer=request.user)
        employee.save()

        data = {'id': employee.id, 'first_name': user.first_name,
                'last_name': user.last_name, 'email': user.email,
                'shop': employee.shop.shop_name}

        return JsonResponse({'user': data})


# update user ajax view
class UpdateUser(View):
    def post(self, request):
        id = request.POST.get('id', None)
        shop_name = request.POST.get('shop', None)

        employee = Employee.objects.get(pk=id)
        shop = request.user.shops.get(shop_name=shop_name)
        employee.shop = shop
        employee.save()


# Create shop ajax view
class CreateShop(View):
    def post(self, request):
        shop_name = request.POST.get('shop_name', None)

        # create shop
        shop = Shop(shop_name=shop_name, owner=request.user)
        shop.save()

        return JsonResponse({'msg': 'Successfull'})


# Update shop Name ajax view
class UpdateShop(View):
    def post(self, request):
        id = request.POST.get('id', None)
        shop_name = request.POST.get('shop', None)

        # get the shop using the id
        shop = request.user.shops.get(pk=id)
        shop.shop_name = shop_name
        shop.save()


# Create category ajax view
class CreateCategory(View):
    def post(self, request):
        category_name = request.POST.get('category_name', None)
        shop_name = request.POST.get('shop_name', None)
        # Getting shop both from employee and employer
        if request.user.is_employed:
            shop = request.user.employee_set.get().shop
        else:
            shop = request.user.shops.get(shop_name=shop_name)

        category = Category(category_name=category_name, shop=shop)
        category.save()

        return JsonResponse({'msg': 'Successfull'})


class CreateItem(View):
    def post(self, request):
        item_name = request.POST.get('item_name', None)
        item_description = request.POST.get('description', None)
        item_quantity = request.POST.get('quantity', None)
        unit_price = request.POST.get('item_price', None)
        purchase_price = request.POST.get('purchase_price', None)
        reorder_level = request.POST.get('reorder_level')
        reoder_quantity = request.POST.get('reorder_quantity', None)
        location = request.POST.get('location', None)
        category_name = request.POST.get('category', None)
        shop_name = request.POST.get('shop', None)

        # getting item value from price and quantity
        value = float(item_quantity) * float(unit_price)

        # get shop from employee
        if request.user.is_employed:
            shop = request.user.employee_set.get().shop
        else:
            shop = request.user.shops.get(shop_name=shop_name)

        # get category
        category = Category.objects.get(category_name=category_name, shop=shop)

        item = Item(item_name=item_name, item_description=item_description,
                    item_quantity=item_quantity, unit_price=unit_price,
                    value=value, purchase_price=purchase_price,
                    reorder_level=reorder_level,
                    reorder_quantity=reoder_quantity,
                    location=location, category=category, shop=shop)
        item.save()

        data = {'id': item.id,
                'item_name': item.item_name,
                'item_description': item.item_description,
                'item_quantity': item.item_quantity,
                'unit_price': item.unit_price,
                'value': item.value,
                'purchase_price': item.purchase_price,
                'reorder_level': item.reorder_level,
                'reorder_quantity': item.reorder_quantity,
                'location': item.location,
                'category': item.category.category_name,
                'shop': item.shop.shop_name}

        return JsonResponse({'item': data})


class EditItem(View):
    def post(self, request, id):
        shop_name = request.POST.get('shop')
        item_name = request.POST.get('item_name')
        item_description = request.POST.get('description')
        item_quantity = request.POST.get('quantity')
        unit_price = request.POST.get('item_price')
        purchase_price = request.POST.get('purchase_price')
        reorder_level = request.POST.get('reorder_level')
        reorder_quantity = request.POST.get('reorder_quantity')
        location = request.POST.get('location')
        category_name = request.POST.get('category')

        # getting item value from price and quantity
        value = float(item_quantity) * float(unit_price)

        # get shop from employee
        if request.user.is_employed:
            shop = request.user.employee_set.get().shop
        else:
            shop = request.user.shops.get(shop_name=shop_name)

        # get category
        category = Category.objects.get(category_name=category_name, shop=shop)

        item = Item.objects.get(id=id)
        item.item_name = item_name
        item.item_description = item_description
        item.item_quantity = item_quantity
        item.unit_price = unit_price
        item.purchase_price = purchase_price
        item.value = value
        item.reorder_level = reorder_level
        item.reorder_quantity = reorder_quantity
        item.location = location
        item.cateogry = category
        item.save()

        if request.user.is_employed:
            return redirect('employee_view')
        else:
            return redirect('view')


# Delete employee ajax view
def delete_employee(request, id):
    employee = Employee.objects.get(pk=id, employer=request.user)
    employee.delete()

    return redirect('users')


# Delete Item ajax view
def delete_item(request, id):
    item = Item.objects.get(pk=id)
    item.delete()

    if request.user.is_employed:
        return redirect('employee_view')
    else:
        return redirect('view')
