from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import TopicForm, EntryForm
from .models import Topic, Entry

def index(request):
    """Página principal do Learning_log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Página que mostra todos os tópicos"""
    topic = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topic}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Mostra um único tópico e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id)
    # Verifica se o tópico pertence ao usuário logado
    if topic.owner != request.user:
        raise Http404
    entries = Entry.objects.filter(topic=topic).order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Adiciona um novo tópico"""
    if request.method != 'POST':
        # Nenhum dado foi enviado; cria um formulário em branco
        form = TopicForm()
    else:
        # Dados foram enviados; processa os dados
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))
    # Exibe um formulário em branco ou exibe mensagens de erro
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Adiciona uma nova entrada para um tópico específico"""
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

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

@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Solicitação inicial; preenche o formulário com os dados atuais
        form = EntryForm(instance=entry)
    else:
        # Dados foram enviados; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.pk]))

    # Exibe um formulário em branco ou exibe mensagens de erro
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)