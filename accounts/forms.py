from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Profile


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Username'}),
                               required=True,)
    email = forms.EmailField(
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Email'}),
                             required=True)
    password1 = forms.CharField(
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Password'}),
                                required=True)
    password2 = forms.CharField(
                                help_text="Password should be similar \
                                    to first one",
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Confirm Password'}),
                                required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'type': 'text',
                                               'class': 'form-control'})
        }


class ProfileUpdateForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = ['phone_no', 'profile_image']
