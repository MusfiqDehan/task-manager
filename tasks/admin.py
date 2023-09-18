from django.contrib import admin
from .models import Task, Photo


class PhotoInline(admin.TabularInline):
    model = Photo


class TaskAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]


admin.site.register(Task, TaskAdmin)
admin.site.register(Photo)
