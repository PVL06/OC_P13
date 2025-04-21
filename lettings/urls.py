"""
URL configuration for the lettings app.

This module defines the URL patterns for the lettings section of the site.
It includes views for listing all lettings and displaying details for a single letting.

Available routes:
- /lettings/ : List all lettings
- /lettings/<letting_id>/ : Display details of a specific letting by ID
"""

from django.urls import path

from lettings import views


urlpatterns = [
    path('', views.index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
