"""
Root URL configuration for the Django project.

This module defines the base URL patterns for the entire site. It includes:
- the homepage,
- the lettings app,
- the profiles app,
- and the Django admin interface.

Routes included:
- / : Homepage view
- /lettings/ : URLs for the lettings app
- /profiles/ : URLs for the profiles app
- /admin/ : Django admin site
"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('error500/', views.error_500)
]
