from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    teachers = models.ManyToManyField(Teacher)
