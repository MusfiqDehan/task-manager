from django import forms
from .models import Task, Photo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description',
                  'due_date', 'priority', 'is_complete']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
