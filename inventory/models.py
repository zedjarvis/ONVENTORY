from django.db import models
from accounts.models import User


# Shops per user
class Shop(models.Model):

    id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='shops')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.shop_name


# Employees per shop
class Employee(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,
                             related_name='employees')
    employer = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='employees', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.user.username


# Categories per shop
class Category(models.Model):

    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,
                             related_name='categories')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.category_name


# Items per category
class Item(models.Model):

    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_description = models.TextField()
    item_quantity = models.DecimalField(
        decimal_places=2, max_digits=12, null=True)
    unit_price = models.DecimalField(
        decimal_places=2, max_digits=12, null=True)
    value = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True)
    purchase_price = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True)
    reorder_level = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True)
    reorder_quantity = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='items', null=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL,
                             related_name='items', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.item_name
