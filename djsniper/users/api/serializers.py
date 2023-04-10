#from django.contrib.auth import get_user_model
#from rest_framework import serializers

#User = get_user_model()


#class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ["username", "name", "url"]

#        extra_kwargs = {
#            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
#        }

from rest_framework import serializers
from .models import User, Role, CustomGroup, CustomPermission, PaymentMethod, CoalBonus, Project, PurchaseOrder


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class CustomGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomGroup
        fields = '__all__'


class CustomPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPermission
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    groups = CustomGroupSerializer(many=True, read_only=True)
    user_permissions = CustomPermissionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('user_id', 'username', 'email', 'name', 'image', 'verified', 'nit', 'role', 'groups', 'user_permissions', 'is_superuser')


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class CoalBonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoalBonus
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    enterprise = UserSerializer()
    developer = UserSerializer()
    investor = UserSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer()
    project = ProjectSerializer()

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
