from django import forms
from core.models import ToDo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email']

class AddTodoForm(forms.ModelForm):
    class Meta:
        pass
        model = ToDo

        fields = ['Date', 'Discreption']
        