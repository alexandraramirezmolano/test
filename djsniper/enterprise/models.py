from django.db import models
from djsniper.users.models import User
from djsniper.sniper.models import NFTProject
# Create your models here.

class Enterprise(User):
    """Enterprise user."""

    project = models.ManyToManyField(NFTProject)
   
    class Meta:
        verbose_name = "Enterprise"
        verbose_name_plural = "Enterprises"

    def __str__(self):
        return self.username