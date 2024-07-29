from django.db import models
from django.contrib.auth.models import User, Group
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    users = models.ManyToManyField(User, through='ProjectUser')

    class Meta:
        permissions = [
            ("can_add_project", "Can add project"),
            ("can_change_project", "Can change project"),
            ("can_delete_project", "Can delete project"),
        ]

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Issue(models.Model):
    summary = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey('Status', on_delete=models.PROTECT)
    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    project = models.ForeignKey('Project', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("can_add_issue", "Can add issue"),
            ("can_change_issue", "Can change issue"),
            ("can_delete_issue", "Can delete issue"),
        ]

    def __str__(self):
        return self.summary

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title



class ProjectUser(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Project Manager'),
        ('lead', 'Team Lead'),
        ('dev', 'Developer'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('project', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.project.name} - {self.role}"
