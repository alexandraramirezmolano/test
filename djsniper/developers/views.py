from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Developer
from djsniper.sniper.models import NFTProject
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import DeveloperProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


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
        return queryset.filter(developer_id=self.request.user.id)


class NFTProjectDetailView(DetailView):
    model = NFTProject
    template_name = 'dashboard/developer/project_detail.html'
    context_object_name = 'project'

class NFTProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = NFTProject
    template_name = 'dashboard/developer/project_update.html'
    form_class = DeveloperProjectForm
    success_url = reverse_lazy('developers:project-list')
 

    def get(self, request, *args, **kwargs):
        # Ensure that only developers or enterprises that created the project can update it
        project = self.get_object()
        if request.user != project.developer_id and request.user != project.enterprise_id:
            return redirect('project-list')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # Set the developer or enterprise that made the update as the new creator
        project = form.save()
        if not project.developer_id and self.request.user != project.enterprise_id:
            project.developer_id = self.request.user
        elif not project.enterprise_id and self.request.user != project.developer_id:
            project.enterprise_id = self.request.user
        project.save()

        return redirect("developer:project-list")

    def get_form_kwargs(self):
        kwargs = super(ProjectCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class ProjectCreateView(generic.CreateView):
    template_name = "dashboard/developer/project_create.html"
    form_class = DeveloperProjectForm

    def form_valid(self, form):
        user = self.request.user
        
        instance = form.save()
    
        return redirect("developer:project-list")

    def get_queryset(self):
        return NFTProject.objects.all()

    def get_form_kwargs(self):
        kwargs = super(ProjectCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
