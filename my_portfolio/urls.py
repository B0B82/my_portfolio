from django.urls import path
from . import views as pv

app_name = 'project'

urlpatterns = [
    path('', pv.portfolio_projects, name='portfolio_projects'),
    path('<int:project_id>/', pv.project_detail, name='project_detail'),
]
