
from django import forms
from django.core.exceptions import ValidationError
from .models import Issue, Status, Type, Project


def validate_no_prohibited_words(value):
    prohibited_words = ['Play', 'Game']
    for word in prohibited_words:
        if word in value:
            raise ValidationError(f"The word '{word}' is not allowed in the summary.")

def validate_description_length(value):
    if len(value) < 10:
        raise ValidationError("The description must be at least 10 characters long.")

class IssueForm(forms.ModelForm):
    summary = forms.CharField(validators=[validate_no_prohibited_words])
    description = forms.CharField(widget=forms.Textarea, validators=[validate_description_length])
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelChoiceField(queryset=Type.objects.all())

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']