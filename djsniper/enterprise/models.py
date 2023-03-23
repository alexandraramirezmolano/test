from django.db import models
from djsniper.sniper.models import NFTProject
# Create your models here.

class Enterprise(models.Model):
    """Enterprise user."""

    project = models.ManyToManyField(NFTProject)
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="developer_profile")
   
    class Meta:
        verbose_name = "Enterprise"
        verbose_name_plural = "Enterprises"

    def __str__(self):
        return self.username