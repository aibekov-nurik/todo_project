from django.db import migrations

def create_test_project(apps):
    Project = apps.get_model('tracker', 'Project')
    Issue = apps.get_model('tracker', 'Issue')

    test_project = Project.objects.create(
        start_date='2024-07-11',
        end_date=None,
        name='Test Project',
        description='This is a test project'
    )

    for issue in Issue.objects.all():
        issue.project = test_project
        issue.save()

class Migration(migrations.Migration):

    dependencies = [
    ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_test_project),
    ]
