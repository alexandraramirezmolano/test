from django.urls import path, include
from . import views

app_name = "enterprise"

urlpatterns = [
   path('projects/<str:username>', views.EnterpriseProjectsView.as_view(), name='enterprise-projects'),
]