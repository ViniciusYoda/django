from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

def logout_view(request):
    """Faz logout do usuário e redireciona para a página inicial."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))
