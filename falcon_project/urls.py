
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('falcon_project.main.urls')),
]
