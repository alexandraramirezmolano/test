from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Developer

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
