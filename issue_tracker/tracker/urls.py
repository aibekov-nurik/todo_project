from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView, add_project_user, delete_project_user,
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/create/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('project/<int:pk>/task/create/', TaskCreateView.as_view(), name='task-create'),
    path('project/<int:pk>/task/update/', TaskUpdateView.as_view(), name='task-update'),
    path('project/<int:pk>/task/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('project/<int:project_id>/add_user/', add_project_user, name='add-project-user'),
    path('project/<int:project_id>/delete_user/', delete_project_user, name='delete-project-user'),
]
