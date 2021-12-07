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
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Confirm Password'}),
                                required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        # Data from form is fetched using clean function
        super(CreateUserForm, self).clean()

        # Getting username
        user_name = self.cleaned_data.get('username')
        password_1 = self.cleaned_data.get('password1')
        password_2 = self.cleaned_data.get('password2')

        # check if username is less than 5 letters
        if len(user_name) < 5:
            self._errors['username'] = self.error_class([
                "Username should be at least 5 characters long"
            ])
        # check if username has whitespace
        if " " in user_name:
            self._errors['username'] = self.error_class([
                "Username should be one word"
            ])
        if password_2 != password_1:
            self._errors['password2'] = self.error_class([
                "password not similar to the first password"
            ])


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = ['phone_no', 'profile_image']
