from django.db import models
from django.db.models import CharField
import uuid
import config



class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name}"

class NFTProject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contract_address = models.CharField(max_length=100)
    contract_abi = models.TextField()
    name = models.CharField(max_length=50)  # e.g BAYC
    number_of_nfts = models.PositiveIntegerField(default=10)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    supply = models.IntegerField(blank=True, default=0)
    price = models.CharField(max_length=200, null=True)
    chain = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    coin = CharField(max_length=20, default="USD", blank=False, editable=False)
    private = models.BooleanField(default=True)
    enterprise_id = models.ForeignKey(config.settings.base.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name="empresa")
    developer = models.ForeignKey(config.settings.base.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name="desarrollador")

    class Meta:
        verbose_name = "Projects"

    def __str__(self):
        return self.name