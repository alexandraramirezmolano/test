from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from djsniper.users.forms import UserChangeForm, UserCreationForm
from .models import User as UserModel, Order, Enterprise, Developer, Investor

User = get_user_model()


# @admin.register(User)
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
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "email", "image", "nit", "allowed", "phone", "contact", "role", "allowed_private_projects"]
    list_editable = ["image", "allowed", "phone", "nit", "contact", "role", "allowed_private_projects"]
    list_filter = [ "allowed", "role", "allowed_private_projects"]
    search_fields = ["username", "name", "email"]
    list_per_page = 15


class UserModelAdmin(admin.ModelAdmin):
    model = UserModel
    list_display = ["username", "name", "email",  "image", "nit", "allowed", "phone", "contact", "role"]
    list_editable = ["image", "allowed", "phone", "nit", "contact", "role"]
    list_filter = ["allowed", "role"]
    search_fields = ["username", "name", "email"]
    list_per_page = 15


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["id", "created", "edited", "nft", "purchase", "bonuses", "voucher", "approved"]
    list_editable = ["voucher","approved"]
    list_filter = ["nft", "approved", "voucher"]
    search_fields = ["nft", "approved"]
    list_per_page = 10

@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    model = Enterprise
    list_display = ('id', 'username', 'email', 'nit', 'role', 'allowed')
    list_editable = ('role', 'allowed')
    search_fields = ('username', 'email', 'nit')
    list_filter = ('role', 'allowed')

@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    model = Investor
    list_display = ('id', 'username', 'email', 'role', 'allowed')
    list_editable = ('role', 'allowed')
    search_fields = ('username', 'email')
    list_filter = ('role', 'allowed')

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    model = Developer
    list_display = ('id', 'username', 'email', 'role', 'allowed_private_projects')
    list_editable = ('role', 'allowed_private_projects')
    search_fields = ('username', 'email')
    list_filter = ('role', 'allowed_private_projects')
    

admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)