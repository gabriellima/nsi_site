from django.shortcuts import render_to_response
from projects.models import Project

def show_all(request):
    projects = Project.objects.all()
    return render_to_response('show_all.html',
      { 'projects': projects,
        'project_count': len(projects) })

