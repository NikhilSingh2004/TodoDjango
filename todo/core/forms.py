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

    def clean(self):
        cleaned_data = super().clean()

        # If 'date_field' is not in the submitted data, set a default value
        if 'Date' not in self.cleaned_data:
            cleaned_data['Date'] = None  # Set your default value here

        return cleaned_data
        