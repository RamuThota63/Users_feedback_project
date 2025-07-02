from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        placeholder_map = {
            'username': 'Enter username',
            'email': 'Enter email address',
            'password1': 'Enter password',
            'password2': 'Re-enter password'
        }
        for field_name, field in self.fields.items():
            field.label = ''
            field.help_text = ''
            field.widget.attrs.update({
                'placeholder': placeholder_map.get(field_name, ''),
                'style': 'border-radius:6px; padding:10px; margin-bottom:10px; width:100%; border:1px solid #ccc;'
            })


class AdminSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(AdminSignupForm, self).__init__(*args, **kwargs)
        placeholder_map = {
            'username': 'Enter admin username',
            'email': 'Enter admin email',
            'password1': 'Enter password',
            'password2': 'Re-enter password'
        }
        for field_name, field in self.fields.items():
            field.label = ''
            field.help_text = ''
            field.widget.attrs.update({
                'placeholder': placeholder_map.get(field_name, ''),
                'style': 'border-radius:6px; padding:10px; margin-bottom:10px; width:100%; border:1px solid #ccc;'
            })


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter username',
            'style': 'border-radius:6px; padding:10px; margin-bottom:10px; width:100%; border:1px solid #ccc;'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter password',
            'style': 'border-radius:6px; padding:10px; margin-bottom:10px; width:100%; border:1px solid #ccc;'
        })
