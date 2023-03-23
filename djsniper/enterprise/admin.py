from django.contrib import admin
from djsniper.developers.models import Developer
from djsniper.users.admin import UserAdmin
from .models import Enterprise

class EnterpriseAdmin(UserAdmin):
    model = Enterprise
    list_display = ["username", "name", "email",  "image", "nit", "allowed", "phone", "contact", "role", "display_projects"]
    list_editable = ["image", "allowed", "phone", "nit", "contact", "role"]
    list_filter = [ "allowed", "role"]
    search_fields = ["username", "name", "email"]
    list_per_page = 15


admin.site.register(Enterprise, EnterpriseAdmin)