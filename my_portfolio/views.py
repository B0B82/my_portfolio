from django.shortcuts import render, get_object_or_404
from .models import Project
from django.http import HttpResponse
from .tasks import *


def index(request):
    # sleepy.delay(10)
    send_email_task()
    return HttpResponse('<h1>Task is done</h1>')


def home(request):
    return render(request, 'my_portfolio/home.html')


def portfolio_projects(request):
    projects = Project.objects.all()
    return render(request, 'my_portfolio/portfolio_projects.html', {'projects': projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'my_portfolio/project_detail.html', {'project': project})

