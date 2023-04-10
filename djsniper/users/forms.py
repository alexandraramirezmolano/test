from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import User
from django import forms
#from djsniper.sniper.models import NFTProject

class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        fields = ["name", "first_name", "last_name", "image"]


class UserChangePassword(admin_forms.PasswordChangeForm):
    class Meta(admin_forms.PasswordChangeForm):
        model = User
        fields = '__all__'


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = '__all__'
        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


