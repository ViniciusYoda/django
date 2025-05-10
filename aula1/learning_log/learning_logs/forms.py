from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    """Um formulário para adicionar um novo assunto"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}  # Remove o rótulo do campo de texto
