from django.urls import path

from tracker.views import IssueListView, IssueDetailView, IssueCreateView, IssueUpdateView, IssueDeleteView
from tracker.views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('', IssueListView.as_view(), name='issue_list'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('issue/create/', IssueCreateView.as_view(), name='issue_create'),
    path('issue/update/<int:pk>/', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/delete/<int:pk>/', IssueDeleteView.as_view(), name='issue_delete'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
]
