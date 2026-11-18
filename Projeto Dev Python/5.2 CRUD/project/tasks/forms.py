from django import forms
from .models import tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = tasks
        fields = ['title', 'description', 'status']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Digite o título da tarefa'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Digite a descrição da tarefa'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }