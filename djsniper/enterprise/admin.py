from django.contrib import admin
from djsniper.users.models import Enterprise
from djsniper.users.admin import UserAdmin


class EnterpriseAdmin(UserAdmin):
    model = Enterprise
    list_display = ["username", "name", "email",  "image", "nit", "allowed", "phone", "contact", "role"]
    list_editable = ["image", "allowed", "phone", "nit", "contact", "role"]
    list_filter = [ "allowed", "role"]
    search_fields = ["username", "name", "email"]
    list_per_page = 15


admin.site.register(Enterprise, EnterpriseAdmin)