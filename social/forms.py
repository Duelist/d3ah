from django import forms
from django.contrib.auth.models import User
from social.models import UserProfile

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=64)
    password = forms.CharField(max_length=64,widget=forms.PasswordInput)

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
                    'password': forms.PasswordInput()
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bnet_id',)