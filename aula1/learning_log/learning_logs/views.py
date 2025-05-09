from django.shortcuts import render
from .models import Topic

def index(request):
    """Página principal do Learning_log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Página que mostra todos os tópicos"""
    topic = Topic.objects.order_by('date_added')
    context = {'topics': topic}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Mostra um único tópico e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)