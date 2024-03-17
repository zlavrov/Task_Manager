from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):

    class Meta:

        model = Task
        fields = ['title', 'content']

        widgets = {
            'title': TextInput(attrs = {
                'class':'form-control',
                'placeholder':'Enter the title'
            }),
            'content': Textarea(attrs = {
                'class':'form-control',
                'placeholder':'Enter a description'
            }),
        }
