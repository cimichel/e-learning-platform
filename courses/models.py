from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
Create Subject, Course and Module models
owner: instructor of the course
subject: subject of the course, it is a foreign key that points to the subject model
title: title of the course.
slug: we will use this for the URL of the course
overview: a text field with brief information about the course
created: date/time are set by Django configuration when creating new objects using auto_now_add=True

Each course is divided into several modules. The Module model contains a foreign key field that points to 
the Course model.
"""


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
