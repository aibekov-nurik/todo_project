from django.contrib.auth.mixins import LoginRequiredMixin
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

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['name', 'description', 'start_date', 'end_date']
    success_url = reverse_lazy('project-list')

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('project-list')

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'projects/task_form.html'
    fields = ['title', 'description', 'project']
    success_url = reverse_lazy('project-list')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'projects/project_detail.html'
    context_object_name = 'task'

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'projects/task_form.html'
    fields = ['title', 'description', 'project']
    success_url = reverse_lazy('project-list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')












