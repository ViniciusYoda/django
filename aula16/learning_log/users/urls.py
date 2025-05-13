from django.urls import path
from . import views


urlpatterns = [
    path('login', view.login, name='login')
    
]
