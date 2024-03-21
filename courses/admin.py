from django.contrib import admin

# Register your models here.
from .models import Subject, Course, Module
'''using decorator @admin.register() to register models in the admin site'''


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['subject', 'created']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ['title']}
    inlines = [ModuleInline]
