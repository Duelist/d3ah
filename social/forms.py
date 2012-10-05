from django import forms
from django.contrib.auth.models import User
from social.models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label=u'Username')
    password = forms.CharField(max_length=32, label=u'Password')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bnet_id',)