from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display      = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_link = ('email', 'first_name', 'last_name')
    readonly_first    = ('last_login', 'date_joined')
    ordering          = ('-date_joined',)

    filter_horizontal = ()
    list_filter       = ()
    fieldsets         = ()

# Register your models here.
admin.site.register(Account, AccountAdmin)  # le decimos q registre la clase Account
#admin.site.register(Account)  # le decimos q registre la clase Account
