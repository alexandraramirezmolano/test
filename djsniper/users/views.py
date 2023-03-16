from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import generic
from django.views.generic import DetailView, RedirectView, UpdateView
from .models import User, Order
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from .forms import UserPersonalCreationForm, UserEnterpriseCreationForm, UserChangeForm, UserChangePassword
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required




class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/dashboard.html"


user_detail_view = UserDetailView.as_view()


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/user_detail.html"


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserPasswordUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserChangePassword
    template_name = "users/password.html"


user_password_view = UserPasswordUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={
            "username": self.request.user.username
        })


user_redirect_view = UserRedirectView.as_view()


class UserPersonalCreateView(generic.CreateView):
    template_name = "account/signup_personal.html"

    # model = User
    form_class = UserPersonalCreationForm

    def form_valid(self, form):
        instance = form.save()
        return redirect("sniper:home")


Role = (
    ('Persona Natural', 'Persona Natural'),
    ('Empresa', 'Empresa'),
    ('Administrador', 'Administrador'),
    ('Desarrollador', 'Desarrollador')
)


class UserEnterpriseCreateView(generic.CreateView):
    template_name = "account/signup_enterprise.html"
    form_class = UserEnterpriseCreationForm
    # model = User
    success_message = _("Informaton successfully updated")
    initial = {
        "role": "Empresa"
    }

    def form_valid(self, form):
        instance = form.save()
        return redirect("sniper:home")


class OrderCreateView(generic.CreateView):
    template_name = "sniper/order_create.html"
    form_class = Order
    success_message = _("Tu orden ha sido listada")


class CustomLoginView(LoginView):
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users/dashboard.html')
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('users/dashboard.html')
        else:
            return self.form_invalid(form)

@method_decorator(login_required, name='dispatch')
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/dashboard.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect('admin_dashboard')
        elif request.user.groups.filter(Role='Empresa').exists():
            return redirect('enterprise_dashboard')
        elif request.user.groups.filter(Role='Persona Natural').exists():
            return redirect('investor_dashboard')
        elif request.user.groups.filter(Role='Desarrollador').exists():
            return redirect('developer_dashboard')
        else:
            return HttpResponse("You don't have permission to access this page.")

@method_decorator(login_required, name='dispatch')
class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/admin_dashboard.html'

@method_decorator(login_required, name='dispatch')
class EnterpriseDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/enterprise.html'

@method_decorator(login_required, name='dispatch')
class InvestorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/dashboard.html'

@method_decorator(login_required, name='dispatch')
class DeveloperDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/developer.html'

class CustomLogoutView(LogoutView):
    template_name = 'account/logout.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'