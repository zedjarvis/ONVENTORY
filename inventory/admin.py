from django.contrib import admin
from .models import (
    Shop,
    Employee,
    Category,
    Item
)


admin.site.register(Shop)
admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(Item)
