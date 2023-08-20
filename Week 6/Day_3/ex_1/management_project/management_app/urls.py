"""
URL configuration for management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import (
    DepartmentListAPIView,
    EmployeeListAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    TaskRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('departments/', DepartmentListAPIView.as_view(), name='department-list'),
    path('employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('departments/<int:pk>/', DepartmentDetailAPIView.as_view(), name='department-detail'),
    path('departments/<int:pk>/', DepartmentDetailAPIView.as_view(), name='department-detail'),
    path('employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
# ... any other URL patterns you have


]
# Repeat for other models...
