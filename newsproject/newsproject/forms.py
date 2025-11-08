from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='Your First Name', required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(max_length=100, label='Your Surname', widget=forms.TextInput(attrs={'class': 'form-input'}))
    subject = forms.CharField(max_length=200, label='Subject', required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Your Email', required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    message = forms.CharField(    
        widget=forms.Textarea(attrs={'class': 'form-input'}),
    )