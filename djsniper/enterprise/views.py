from django.shortcuts import render
from djsniper.sniper.models import NFTProject
# Create your views here.
from django.views.generic.list import ListView
from django.views import generic


class EnterpriseProjectsView(generic.ListView):
    template_name = "dashboard/enterprise/projects_list.html"
    model = NFTProject

    def get_queryset(self):
        return NFTProject.objects.all()


    def filter_by_enteprise(self, enterprise=self.request.user.id):
        filtered_projects = []
        for project in self.projects:
            if project.enterprise == enterprise:
                filtered_projects.append(project)
                grouped_objects = filtered_projects
        return print(grouped_objects)