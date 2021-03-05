from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    return render(request, 'my_portfolio/home.html')


def portfolio_projects(request):
    projects = Project.objects.all()
    return render(request, 'my_portfolio/portfolio_projects.html', {'projects': projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'my_portfolio/project_detail.html', {'project': project})
