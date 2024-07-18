from django import forms

from tracker.models import Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['start_date', 'end_date', 'name', 'description']
