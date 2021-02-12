from django.contrib import admin
from accounts.models import User, user_type 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
#admin.site.register(Account)

class UserAdmin(BaseUserAdmin):
    fieldsets = (
            (None, {'fields': ('email', 'password', 'username', 'last_login')}),
            ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
            )}),
        )
    add_fieldsets = (
        (
        None,
            {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
            }
        ),
    )
    list_display = ('email', 'username', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    
admin.site.register(User, UserAdmin)
admin.site.register(user_type)