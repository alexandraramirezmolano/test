from django.urls import path
from .views import DeveloperListView, DeveloperCreateView, DeveloperUpdateView, DeveloperDetailView, NFTProjectListView, NFTProjectDetailView

app_name = 'developers'

urlpatterns = [
    path('', DeveloperListView.as_view(), name='developers-list'),
    path('create/', DeveloperCreateView.as_view(), name='developer-create'),
    path('<int:pk>/update/', DeveloperUpdateView.as_view(), name='developer-update'),
    path('<int:pk>/', DeveloperDetailView.as_view(), name='developer-detail'),

    path('projects-list/', NFTProjectListView.as_view(), name='project-list'),
    path('project/<uuid:pk>/', NFTProjectDetailView.as_view(), name='project-detail')
]