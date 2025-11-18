from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Enter your email', 'id': 'email'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Tell us about yourself', 'rows': 4}))
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Choose a username', 'id': 'username'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name', 'id': 'firstName'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name', 'id': 'lastName'}))
    password1 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Enter your password', 'id': 'password'}))
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Confirm your password', 'id': 'confirmPassword'}))
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'specialization', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'specialization': forms.Select(attrs={'class': 'form-select', 'id': 'specialization'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1']) 
        if commit:
            user.save()
        return user



class CustomUserAutorizationForm(AuthenticationForm):
    username = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Enter your email', 'id': 'email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Enter your password', 'id': 'password'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id': 'rememberMe'}))
    class Meta:
        model = CustomUser


class UserSettingsForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Enter your email', 'id': 'email'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Tell us about yourself', 'rows': 4}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name', 'id': 'firstName'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name', 'id': 'lastName'}))
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'bio', 'specialization']
        widgets = {
            'specialization': forms.Select(attrs={'class': 'form-select', 'id': 'specialization'}),
        }        