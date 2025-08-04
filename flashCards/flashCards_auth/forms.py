from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        min_length=4,
        max_length=30,
        widget=forms.EmailInput(attrs={'class': 'border rounded-lg p-2 w-full'})
    )
    username = forms.CharField(
        label='Username',
        min_length=4,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'border rounded-lg p-2 w-full'})
    )

    password1 = forms.CharField(
        label='Password',
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput(attrs={'class': 'border rounded-lg p-2 w-full'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput(attrs={'class': 'border rounded-lg p-2 w-full'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        min_length=4,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'border rounded-lg p-2 w-full'})
    )
    password = forms.CharField(
        label='Password',
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput(attrs={'class': 'border rounded-lg p-2 w-full'})
    )
