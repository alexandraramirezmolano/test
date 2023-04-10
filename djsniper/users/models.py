from django.db import models
from django.contrib.auth.models import AbstractUser, Group, PermissionsMixin, Permission
import uuid


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.TextField()
    buy = models.BooleanField(default=False)
    sell = models.BooleanField(default=False)
    create = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    list = models.BooleanField(default=False)


class CustomGroup(Group):
    class Meta:
        proxy = True


class CustomPermission(Permission):
    class Meta:
        proxy = True


class User(AbstractUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    image = models.ImageField()
    verified = models.BooleanField(default=False)
    nit = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True, related_name='users')
    groups = models.ManyToManyField(Group, blank=True, related_name='user_set', through='CustomGroup')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_set',
                                              through='CustomPermission')
    groups = models.ManyToManyField(
        CustomGroup,
        verbose_name=('groups'),
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    user_permissions = models.ManyToManyField(
        CustomPermission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )


class PaymentMethod(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.TextField()
    api_key = models.TextField()


class CoalBonus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    contract = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='coal_bonuses')


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.TextField()
    description = models.TextField()
    contract = models.TextField()
    image = models.ImageField()
    coal_bonuses = models.ForeignKey(CoalBonus, on_delete=models.CASCADE)
    bonuses_quantity = models.IntegerField()
    price = models.FloatField()
    blockchain = models.TextField()
    private = models.BooleanField(default=False)
    enterprise = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enterprise_projects')
    developer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='developer_projects')
    investor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investor_projects')
    verified = models.BooleanField(default=False)
    ton_of_carbon_equivalent = models.IntegerField()

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_orders')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    bonuses_quantity = models.IntegerField()
    purchase_value = models.FloatField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.username}'s order for {self.project.name}"