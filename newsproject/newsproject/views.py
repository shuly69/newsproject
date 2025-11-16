from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
def contacts(request):
    breadcrumb = 'Contacts'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['']   
            )
            return render(request, 'info-pages/contacts.html', {
                'breadcrumb': breadcrumb,
                'form': ContactForm(),
                'success': True
            })
        else:
            return render(request, 'info-pages/contacts.html', {
                'breadcrumb': breadcrumb,
                'form': form,
                'success': False
            })
    else:
        form = ContactForm()
        # Handle contact form submission logic here
        
        return render(request, 'info-pages/contacts.html', {'breadcrumb': breadcrumb, 'form': form})

def about_us(request):
    breadcrumb = 'About Us'
    return render(request, 'info-pages/about-us.html', {'breadcrumb': breadcrumb})

def privacy_policy(request):
    breadcrumb = 'Privacy Policy'
    return render(request, 'info-pages/privacy-policy.html', {'breadcrumb': breadcrumb})

def terms_of_service(request):
    breadcrumb = 'Terms of Service'
    return render(request, 'info-pages/terms.html', {'breadcrumb': breadcrumb})