from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

base_attrs = (
    'block w-full text-gray-700 rounded-lg px-3 py-2 my-2 border-none outline-none border-2 bg-gray-300 focus:bg-gray-100'
)


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': base_attrs, 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': base_attrs, 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update(
            {'class': base_attrs, 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': base_attrs, 'placeholder': 'Repeat Password'})


class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': base_attrs,
            'placeholder': 'Username',
        })
        self.fields['password'].widget.attrs.update({
            'class': base_attrs,
            'placeholder': 'Password',
        })
