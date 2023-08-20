from django.shortcuts import render
from rest_framework import generics
from .models import Department, Employee, Project, Task
from .serializers import DepartmentSerializer, EmployeeSerializer, ProjectSerializer, TaskSerializer

class DepartmentListAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeListAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Create your views here.
from .permissions import IsDepartmentAdmin

class DepartmentListAPIView(generics.ListAPIView):
    ...
    permission_classes = [IsDepartmentAdmin]

class DepartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    ...
    permission_classes = [IsDepartmentAdmin]

class EmployeeListAPIView(generics.ListAPIView):
    ...
    permission_classes = [IsDepartmentAdmin]

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    ...
    permission_classes = [IsDepartmentAdmin]

class TaskListAPIView(generics.ListAPIView):
    ...
    permission_classes = [IsDepartmentAdmin]

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    ...
    permission_classes = [IsDepartmentAdmin]

from .serializers import DepartmentHyperlinkedSerializer, EmployeeHyperlinkedSerializer, TaskHyperlinkedSerializer

class DepartmentListAPIView(generics.ListAPIView):
    ...
    serializer_class = DepartmentHyperlinkedSerializer

class DepartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    ...
    serializer_class = DepartmentHyperlinkedSerializer

class EmployeeListAPIView(generics.ListAPIView):
    ...
    serializer_class = EmployeeHyperlinkedSerializer

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    ...
    serializer_class = EmployeeHyperlinkedSerializer

class TaskListAPIView(generics.ListAPIView):
    ...
    serializer_class = TaskHyperlinkedSerializer

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    ...
    serializer_class = TaskHyperlinkedSerializer
