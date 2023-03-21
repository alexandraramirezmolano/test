from django.contrib import admin
from .models import NFTProject, NFT, NFTTrait, NFTAttribute, Category


class NFTAdmin(admin.ModelAdmin):
    model = NFT
    list_display = ["nft_id", "rank", "rarity_score", "image"]
    search_fields = ["nft_id__exact", "rank", "rarity_score"]
    list_filter = ["rank", "rarity_score"]
    list_per_page = 15
    search_help_text = "Buscar por ranking o score"


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["id", "name", "image", "created", "edited"]
    search_fields = ["id", "name"]
    list_filter = ["name", "edited"]
    list_per_page = 15
    search_help_text = "Buscar por nombre o última fecha de edición"


class NFTAttributeAdmin(admin.ModelAdmin):
    model = NFTAttribute
    list_display = ["value"]
    list_per_page = 15


class NFTProjectAdmin(admin.ModelAdmin):
    model = NFTProject

    def get_model_fields(self):
        return self.model._meta.get_fields()

    list_per_page = 15
    list_display = [field.name for field in self.get_model_fields()]
    list_filter = list_display
    search_fields = list_display
    search_help_text = ["Buscar por {}".format(field.verbose_name) for field in self.get_model_fields()]




class NFTTraitAdmin(admin.ModelAdmin):
    model = NFTTrait
    list_display = ["rarity_score"]
    list_filter = ["rarity_score"]
    list_per_page = 15
    search_fields = ["rarity_score"]
    search_help_text = "Buscar por score"


admin.site.register(NFTProject, NFTProjectAdmin)
admin.site.register(NFTTrait, NFTTraitAdmin)
admin.site.register(NFT, NFTAdmin)
admin.site.register(NFTAttribute, NFTAttributeAdmin)
admin.site.register(Category, CategoryAdmin)
