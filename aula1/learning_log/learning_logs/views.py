from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TopicForm, EntryForm
from .models import Topic, Entry

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

def new_entry(request, topic_id):
    """Adiciona uma nova entrada para um tópico específico"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Nenhum dado foi enviado; cria um formulário em branco
        form = EntryForm()
    else:
        # Dados foram enviados; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    # Exibe um formulário em branco ou exibe mensagens de erro
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edita uma entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Solicitação inicial; preenche o formulário com os dados atuais
        form = EntryForm(instance=entry)
    else:
        # Dados foram enviados; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))

    # Exibe um formulário em branco ou exibe mensagens de erro
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)