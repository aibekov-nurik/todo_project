from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project, Task

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['name', 'description', 'start_date', 'end_date']
    success_url = reverse_lazy('project-list')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('project-list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')

class TaskCreateView(CreateView):
    model = Task
    template_name = 'projects/task_form.html'
    fields = ['title', 'description', 'project']
    success_url = reverse_lazy('project-list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'projects/task_form.html'
    fields = ['title', 'description', 'project']
    success_url = reverse_lazy('project-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project-list')


