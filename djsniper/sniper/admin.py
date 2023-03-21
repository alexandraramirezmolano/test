from django.contrib import admin
from .models import NFTProject, NFT,  NFTAttribute, Category


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




class NFTProjectAdmin(admin.ModelAdmin):
    model = NFTProject

    list_display = ['id', 'name', 'number_of_nfts', 'category', 'supply', 'price', 'chain', 'description', 'coin', 'private']

    list_filter = list_display
    search_fields = list_display






admin.site.register(NFTProject, NFTProjectAdmin)

admin.site.register(NFT, NFTAdmin)

admin.site.register(Category, CategoryAdmin)
