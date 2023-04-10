from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from djsniper.users.forms import UserChangeForm, UserCreationForm
from .models import User as Role, User, PaymentMethod, CoalBonus, Project, PurchaseOrder

User = get_user_model()


#@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
    #list_display = ["username", "name", "email", "image", "nit", "allowed", "phone", "contact", "role"]
    #list_display = '__all__'
    #list_editable = ["image", "allowed", "phone", "nit", "contact", "role"]
    #list_filter = [ "allowed", "role"]
    #search_fields = ["username", "name", "email"]
    list_display = ['user_id', 'name', 'last_name', 'verified', 'nit']
    list_filter = ['verified']
    search_fields = ['name', 'last_name', 'nit']
    list_per_page = 15

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'api_key']
    search_fields = ['name']

@admin.register(CoalBonus)
class CoalBonusAdmin(admin.ModelAdmin):
    list_display = ['id', 'contract', 'owner']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'enterprise', 'developer', 'investor', 'price']
    list_filter = ['private', 'verified']
    search_fields = ['name', 'description', 'blockchain']
    autocomplete_fields = ['enterprise', 'developer', 'investor']
    fieldsets = [
        [None, {
            'fields': ['name', 'description', 'contract', 'image', 'coal_bonuses', 'bonuses_quantity', 'price', 'blockchain', 'ton_of_carbon_equivalent']
        }],
        ['Privacy', {
            'fields': ['private',]
        }],
        ['Verification', {
            'fields': ['verified',]
        }],
        ['Users', {
            'fields': ['enterprise', 'developer', 'investor']
        }],
    ]

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'project', 'bonuses_quantity', 'purchase_value', 'payment_method', 'verified']
    list_filter = ['verified',]
    search_fields = ['customer__name', 'project__name']
    autocomplete_fields = ['customer', 'project', 'payment_method']
    search_fields = ['id','name']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']