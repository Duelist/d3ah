from django import forms
from social.models import AppUser

class AppUserForm(forms.Form):
    email = forms.EmailField(max_length=64,
                             required=True,
                             error_messages={'required': 'Required'})
    password = forms.CharField(max_length=64,
                               widget=forms.PasswordInput,
                               required=True,
                               error_messages={'required': 'Required'})
    password_confirm = forms.CharField(max_length=64,
                                       widget=forms.PasswordInput,
                                       required=True,
                                       error_messages={'required': 'Required'})

    def clean(self):
        cleaned_data = super(AppUserForm, self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError('Password mismatch.')

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32,
                               required=True)
    password = forms.CharField(max_length=64,
                               widget=forms.PasswordInput,
                               required=True)

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=32,
                               required=True,
                               error_messages={'required': 'Required'})
    email = forms.EmailField(max_length=64,
                             required=True,
                             error_messages={'required': 'Required'})
    password = forms.CharField(max_length=64,
                               widget=forms.PasswordInput,
                               required=True,
                               error_messages={'required': 'Required'})
    password_confirm = forms.CharField(max_length=64,
                                       widget=forms.PasswordInput,
                                       required=True,
                                       error_messages={'required': 'Required'})

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError('Password mismatch.')

        return cleaned_data