import json
import sys
from operator import attrgetter
from django.contrib.auth.mixins import LoginRequiredMixin
from celery.result import AsyncResult
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.detail import SingleObjectMixin, View
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from djsniper.developers.forms import  DeveloperProjectForm
from djsniper.sniper.models import NFTProject, Category
#from djsniper.sniper.tasks import fetch_nfts_task
from djsniper.enterprise.forms import EnterpriseProjectForm
from rest_framework import viewsets
from djsniper.sniper.api import serializers
from djsniper.users.forms import OrderCreationForm, OrderUpdateForm
from djsniper.users.models import Order, User
from django.views.generic.edit import ModelFormMixin
from djsniper.users.api.serializers import OrderSerializer
from itertools import groupby

sys.setrecursionlimit(10000)


class HomeCategoriesListView(generic.ListView):
    template_name = "base.html"

    def get_queryset(self):
        return Category.objects.all()


def ChooseRole(request):
    return render(request, "account/choose_role.html")


class ProjectViewset(viewsets.ModelViewSet):
    queryset = NFTProject.objects.all()
    serializer_class = serializers.NFTProjectSerializer

    def get_queryset(self):
        project = NFTProject.objects.all()

        name = self.request.GET.get('name')

        if name:

            project = project.filter(name__contains=name)

        else:

            return project


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        category = Category.objects.all()

        name = self.request.GET.get('name')

        if name:

            category = category.filter(name__contains=name)

        else:

            return category

class OrdersViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        category = Category.objects.all()


class ProjectListView(generic.ListView):
    template_name = "sniper/project_list.html"

    def get_queryset(self):
        return NFTProject.objects.all()


class EnterpriseProjectsView(LoginRequiredMixin, ListView):
    model = NFTProject
    template_name = 'dashboard/enterprise/projects_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(enterprise=self.request.user.id)

class UserProjectsView(generic.ListView):
    template_name = "users/my_projects.html"
    model = Order

    def __init__(self):
        self.orders = Order.objects.all()

    def group_by_project(self):
        grouped_orders = {}
        for order in self.orders:
            if order.nft not in grouped_orders:
                grouped_orders[order.nft] = []
            grouped_orders[order.nft].append(order)
        return print(grouped_orders)

    def filter_by_approval(self, approved=True):
        filtered_orders = []
        for order in self.orders:
            if order.approved == approved:
                filtered_orders.append(order)
                grouped_objects = filtered_orders
        return print(grouped_objects)


class UserBillingsView(generic.ListView):
    template_name = "users/billings.html"

    def get_queryset(self):
        return Order.objects.all()


class UserPaymentsHistoryView(generic.ListView):
    template_name = "users/payments_history.html"

    def get_queryset(self):
        return Order.objects.all()




class ProjectDetailView(ModelFormMixin, generic.DetailView):
    model = NFTProject
    template_name = 'sniper/project_detail.html'
    form_class = OrderCreationForm

    # no get_context_data override

    def post(self, request, *args, **kwargs):
        # first construct the form to avoid using it as instance
        form = self.get_form()
        user = request.user
        nft_project = self.get_object()

        if form.is_valid():
            # instance = form.save()
            NFTProject.objects.filter(pk=nft_project.id).update(
                supply=int(int(nft_project.supply) - int(form.cleaned_data["bonuses"])))
            user.project.add(nft_project.id)
            # form.cleaned_data["purchase"] = nft_project.price * form.cleaned_data["bonuses"]
            # form = nft_project.price * form.cleaned_data["bonuses"]
            # instance = form.save()
            # updateProjectSupply(project, instance.bonuses)
            print(form)
            instance = form.save()
            Order.objects.filter(pk=instance.id).update(
                purchase=int(int(nft_project.price) * int(form.cleaned_data["bonuses"])))
            return redirect("sniper:home")
        else:
            print(form)
            return super(ProjectDetailView, self.get_object()).form_invalid(form)

            # return form

    def get_success_url(self):
        return redirect("sniper:home")


class OrderCreateView(generic.CreateView):
    template_name = "sniper/order_create.html"
    form_class = OrderCreationForm
    model = NFTProject

    def form_valid(self, form):
        # instance = form.save()
        # nft_project = self.get_object()
        # NFTProject.objects.filter(pk=nft_project.id).update(supply=('supply') - instance.bonuses)
        # instance = form.save()
        # updateProjectSupply(project, instance.bonuses)
        return redirect("sniper:home")

    def get_queryset(self):
        return Order.objects.all()

class ProjectCreateView(generic.CreateView):
    template_name = "sniper/project_create.html"

    def form_valid(self, form):
        user = self.request.user
        
        instance = form.save()
        if user.role == "Desarrollador":
            pass
        elif user.role == "Empresa":
            return redirect("enterprise:enterprise-projects", username=self.request.user.username)

    def get_queryset(self):
        return NFTProject.objects.all()

    def get_form_class(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == "Desarrollador":
                return DeveloperProjectForm
            elif user.role == "Empresa":
                form_class = EnterpriseProjectForm
                form_class.base_fields['enterprise_id'].initial = user.id
                return form_class
        # Default form class
        return EnterpriseProjectForm



class ProjectUpdateView(generic.UpdateView):
    template_name = "sniper/project_update.html"

    def get_queryset(self):
        return NFTProject.objects.all()

    def get_success_url(self):
        return reverse("sniper:project-detail", kwargs={"pk": self.get_object().id})

    def get_form_class(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == "Desarrollador":
                return DeveloperProjectForm
            elif user.role == "Empresa":
                return EnterpriseProjectForm
        # Default form class
        return EnterpriseProjectForm


class OrderUpdateView(generic.UpdateView):
    template_name = "users/add_voucher.html"
    form_class = OrderUpdateForm

    def get_queryset(self):
        return Order.objects.all()

    def get_success_url(self):
        return reverse("sniper:home")  # , kwargs={"username": self.get_object().id})


class VoucherDetailView(generic.DetailView):
    template_name = "users/show_voucher.html"

    def get_queryset(self):
        return Order.objects.all()


class ProjectDeleteView(generic.DeleteView):
    template_name = "sniper/project_delete.html"

    def get_queryset(self):
        return NFTProject.objects.all()

    def get_success_url(self):
        return reverse("sniper:project-list")

