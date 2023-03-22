from django.urls import path
from .views import DeveloperListView, DeveloperCreateView, DeveloperUpdateView, DeveloperDetailView

app_name = 'developers'

urlpatterns = [
    path('developers/', DeveloperListView.as_view(), name='developers-list'),
    path('developer-create/', DeveloperCreateView.as_view(), name='developer-create'),
    path('<int:pk>/update/', DeveloperUpdateView.as_view(), name='developer-update'),
    path('<int:pk>/', DeveloperDetailView.as_view(), name='developer-detail'),
]