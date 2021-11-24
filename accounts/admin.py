from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Notification
from django.contrib.auth import get_user_model


# Custom user model admin config
class UserAdminConfig(UserAdmin):
    model = get_user_model()
    search_fields = ('email', 'username', 'first_name',
                     'last_name')

    list_filter = (
                   'is_active', 'is_staff', 'is_superuser')
    ordering = ('-date_joined',)

    list_display = ('email', 'username',
                    'first_name', 'last_name',
                    'is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email',
                           'username',
                           'first_name',
                           'last_name',)}),
        ('Permissions', {'fields': ('is_staff',
                                    'is_active',
                                    'is_superuser',)}),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Profile)
admin.site.register(Notification)
