from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Developer
from djsniper.sniper.models import NFTProject
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


class DeveloperListView(ListView):
    model = Developer
    template_name = 'dashboard/enterprise/developer_list.html'

class DeveloperCreateView(CreateView):
    model = Developer
    fields = '__all__'
    template_name = 'dashboard/enterprise/developer_form.html'
    success_url = reverse_lazy('developers:list')

class DeveloperUpdateView(UpdateView):
    model = Developer
    fields = '__all__'
    template_name = 'dashboard/enterprise/developer_form.html'
    success_url = reverse_lazy('developers:list')

class DeveloperDetailView(DetailView):
    model = Developer
    template_name = 'dashboard/enterprise/developer_detail.html'

class NFTProjectListView(ListView):
    model = NFTProject
    template_name = 'dashboard/developer/project_list.html'
    context_object_name = 'projects'
    ordering = ['-id']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(developer=self.request.user.id)

        
class NFTProjectDetailView(DetailView):
    model = NFTProject
    template_name = 'dashboard/developer/project_detail.html'
    context_object_name = 'project'