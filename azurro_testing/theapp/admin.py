from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EnterpriseUser

@admin.register(EnterpriseUser)
class EnterpriseUserAdmin(UserAdmin):
    # Ensure the non-editable `uuid` field is excluded or marked as read-only
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('company_name',)}),  # Exclude `uuid`
    )
    readonly_fields = ('uuid',)  # Make `uuid` read-only
    list_display = ('username', 'email', 'company_name', 'is_staff', 'uuid')
