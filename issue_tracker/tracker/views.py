
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Issue
from .forms import IssueForm

class IssueListView(ListView):
    model = Issue
    template_name = 'issue_list.html'
    context_object_name = 'issues'

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issue_detail.html'
    context_object_name = 'issue'

class IssueCreateView(CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue_form.html'
    success_url = reverse_lazy('issue_list')

class IssueUpdateView(UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue_form.html'
    success_url = reverse_lazy('issue_list')

class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issue_confirm_delete.html'
    success_url = reverse_lazy('issue_list')
