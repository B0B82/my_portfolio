from django.urls import path
from . import views as bv

app_name = 'blog'

urlpatterns = [
    path('', bv.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', bv.detail, name='detail'),
]
