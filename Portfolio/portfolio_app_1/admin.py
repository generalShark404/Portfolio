from django.contrib import admin
from . models import Project, ProjectImages, ProjectFeature, Person
# Register your models here.

class ProjectImageInline(admin.TabularInline):
    model = ProjectImages
    extra = 1

class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, ProjectFeatureInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Person)