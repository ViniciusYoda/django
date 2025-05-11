from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Um formulário para adicionar um novo assunto"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}  # Remove o rótulo do campo de texto

class EntryForm(forms.ModelForm):   
    """Um formulário para adicionar uma nova entrada"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}  # Remove o rótulo do campo de texto
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # Define a largura do campo de texto