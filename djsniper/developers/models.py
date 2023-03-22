from django.db import models
from djsniper.users.models import User, Enterprise
from djsniper.sniper.models import NFTProject
# Create your models here.


class Developer(User):
    """Developer user."""
    
    enterprise = models.ManyToManyField(Enterprise)
    project = models.ManyToManyField(NFTProject)
    allowed_private_projects = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Developer"
        verbose_name_plural = "Developers"

    def __str__(self):
        return self.username