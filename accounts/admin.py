from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, EmailOTP

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'role', 'is_active', 'is_verified']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_verified', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role'),
        }),
    )
    search_fields = ['email']

    # ✅ This removes the Recent Actions sidebar
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_recent_actions'] = False
        return super().change_view(request, object_id, form_url, extra_context)

admin.site.register(User, CustomUserAdmin)
# Remove Recent Actions from admin index
from django.contrib.admin import AdminSite
AdminSite.index_template = 'admin/custom_index.html'