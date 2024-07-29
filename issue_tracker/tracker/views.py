from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Project, ProjectUser
from .forms import ProjectUserForm, ProjectUserDeleteForm

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


# views.py


@login_required
@permission_required('app.add_project', raise_exception=True)
def add_project_user(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectUserForm(request.POST)
        if form.is_valid():
            project_user = form.save(commit=False)
            project_user.project = project
            project_user.save()
            return redirect('project-detail', project_id=project_id)
    else:
        form = ProjectUserForm()
    return render(request, 'add_project_user.html', {'form': form, 'project': project})

@login_required
@permission_required('app.delete_project', raise_exception=True)
def delete_project_user(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectUserDeleteForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            ProjectUser.objects.filter(project=project, user=user).delete()
            return redirect('project-detail', project_id=project_id)
    else:
        form = ProjectUserDeleteForm()
    return render(request, 'delete_project_user.html', {'form': form, 'project': project})











