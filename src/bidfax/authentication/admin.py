from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from bidfax.authentication.models import User, Profile
from bidfax.authentication.forms import UserCreationForm


class UserAdmin(DefaultUserAdmin):
    add_form = UserCreationForm
    model = User
    list_display = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'uid')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_staff',
                'is_active', 'groups', 'user_permissions'
            )
        }
        ),
    )
    readonly_fields = ('uid',)
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
