from django.contrib import admin
from .models import Account
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'email', 'username', 'is_active', 'is_login', 'is_staff',)
    list_display_links=('first_name', 'last_name', 'email', 'username',)

admin.site.register(Account, AccountAdmin)
