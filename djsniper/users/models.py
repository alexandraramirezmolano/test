from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db.models import CharField, EmailField, ImageField, DateField, AutoField, ManyToManyField, BooleanField, \
    ForeignKey, \
    PROTECT
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from djsniper.sniper.models import NFTProject
from django.db import models
import uuid

Role = (
    ('Persona Natural', 'Persona Natural'),
    ('Empresa', 'Empresa'),
    ('Administrador', 'Administrador'),
    ('Desarrollador', 'Desarrollador')
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser, PermissionsMixin):
    """Default user for djsniper."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(max_length=30, null=True, blank=True)
    last_name = CharField(max_length=30, null=True, blank=True)
    nit = CharField(max_length=30, null=True)
    image = ImageField(blank=True, null=True, upload_to='images/userimage')
    edited = DateField(auto_now=True)
    allowed = BooleanField(default=False)
    project = ManyToManyField(NFTProject)
    role = CharField(max_length=20, choices=Role, default="Persona Natural", blank=True, editable=True)
    phone = CharField(max_length=30, null=True)
    contact = CharField(max_length=50, null=True)
    allowed_private_projects = BooleanField(default=False)
    objects = MyUserManager()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class Order(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)
    nft = models.ForeignKey(NFTProject, on_delete=models.CASCADE, related_name="nft")
    purchase = models.CharField(max_length=200, null=True)
    bonuses = models.IntegerField(blank=True)
    voucher = ImageField(blank=True, null=True, upload_to='images/voucher')
    approved = BooleanField(default=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
