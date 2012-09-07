from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label=u'Username')
    password = forms.CharField(max_length=32, label=u'Password')