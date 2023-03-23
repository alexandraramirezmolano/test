from django.db import models

from djsniper.enterprise.models import Enterprise
from djsniper.sniper.models import NFTProject
# Create your models here.


class Developer(models.Models):
    """Developer user."""
    
    enterprise = models.ManyToManyField(Enterprise)
    project = models.ManyToManyField(NFTProject)
    allowed_private_projects = models.BooleanField(default=False)
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="developer_profile")

    class Meta:
        verbose_name = "Developer"
        verbose_name_plural = "Developers"

    def __str__(self):
        return self.username