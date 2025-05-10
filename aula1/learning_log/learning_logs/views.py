from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TopicForm
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

def new_topic(request):
    """Adiciona um novo tópico"""
    if request.method != 'POST':
        # Nenhum dado foi enviado; cria um formulário em branco
        form = TopicForm()
    else:
        # Dados foram enviados; processa os dados
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    # Exibe um formulário em branco ou exibe mensagens de erro
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)