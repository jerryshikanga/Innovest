from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustonUserCreationForm(UserCreationForm):
    """docstring for CustonUserCreationForm."""
    email = forms.EmailField(required=True)

    class Meta :
        """docstring for Meta """
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
