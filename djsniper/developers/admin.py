from django.contrib import admin
from .models import Developer
# Register your models here.
class DeveloperAdmin(UserAdmin):
    model = Developer
    list_display = ["username", "name", "email", "image", "nit", "allowed", "phone", "contact", "role", "allowed_private_projects"]
    list_editable = ["image", "allowed", "phone", "nit", "contact", "role", "allowed_private_projects"]
    list_filter = [ "allowed", "role", "allowed_private_projects"]
    search_fields = ["username", "name", "email"]
    list_per_page = 15

admin.site.register(Developer, DeveloperAdmin)