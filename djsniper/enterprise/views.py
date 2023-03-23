from django.shortcuts import render
from djsniper.sniper.models import NFTProject
# Create your views here.
from django.views.generic.list import ListView
from django.views import generic

class EnterpriseProjectsView(generic.ListView):
    template_name = "dashboard/enterprise/projects_list.html"
    model = NFTProject

    def get_queryset(self):
        enterprise_id = self.request.user.id
        if enterprise_id:
            return self.model.objects.filter(enterprise_id=enterprise_id)
        else:
            return self.model.objects.all()

    def filter_by_enterprise(self, enterprise=None):
        filtered_projects = []
        queryset = self.get_queryset()
        for project in queryset:
            if project.enterprise_id == enterprise:
                filtered_projects.append(project)
        return filtered_projects
