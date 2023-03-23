from django.shortcuts import render
from djsniper.sniper.models import NFTProject
from django.views.generic.list import ListView
from django.views import generic


class EnterpriseProjectsView(ListView):
    template_name = "dashboard/enterprise/projects_list.html"
    model = NFTProject

    def get_queryset(self):
        return NFTProject.objects.all()

    def filter_by_enteprise(self, enterprise=None):
        enterprise = enterprise or self.request.user.id
        filtered_projects = []
        for project in self.projects:
            if project.enterprise == enterprise:
                filtered_projects.append(project)
        return filtered_projects
