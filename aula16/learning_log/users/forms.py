# from django.contrib.auth.models import User
from django import forms
from django.core.execeptions import ValidationError

# class LoginForm(forms.ModelForm):
#     class Meta: 
#         model = User
#         fields = ['username', 'password']
#         labels = {'username':'Login', 'password':'Senha'}

class LoginForm(forms.Form):
    err
    login = forms.CharField(max_length=30)
    senha = forms.CharField(max_length=30, widget=forms.PasswordInput())

    """def clean(self):
            cleaned_data = super().clean()
            nome = cleaned_data.get('login')
            senha = cleaned_data.get('senha')

            validação
        """

    def clean_login(self):
        nome = self.cleaned_data['login']

        if not(nome.isalnum()):
            raise = ValidationError('O nome de usuário não pode ter caractere especial')
        
        return nome