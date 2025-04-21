"""
URL configuration for the profiles app.

This module defines the URL patterns for the profiles section of the site.
It includes views for listing all profiles and viewing an individual profile.

Available routes:
- /profiles/ : List all profiles
- /profiles/<username>/ : Display a specific user's profile
"""

from django.urls import path

from profiles import views


urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
