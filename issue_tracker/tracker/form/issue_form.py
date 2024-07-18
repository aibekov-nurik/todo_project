from django import forms

from tracker.models import Status, Type, Project, Issue


class IssueForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelChoiceField(queryset=Type.objects.all())
    project = forms.ModelChoiceField(queryset=Project.objects.all())

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type', 'project']
