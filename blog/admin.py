from django.contrib import admin
from .models import Blog

admin.site.register(Blog)  #, verbose_name='Blog')
