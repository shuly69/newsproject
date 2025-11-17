from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserAutorizationForm, UserSettingsForm   
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import CustomUser as Custom_user
from articles.models import Articles as Article
# Create your views here.
def register(request):
    breadcrumb = 'Register'
    if request.method == 'POST':
        form = CustomUserCreationForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'users/register.html', {'form': form, 'breadcrumb': breadcrumb})
    else:
        form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form, 'breadcrumb': breadcrumb})

def login(request):
    breadcrumb = 'Login'
    if request.method == 'POST':
        form = CustomUserAutorizationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if not form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)  # Session expires on browser close
            else:
                request.session.set_expiry(1209600)  # 2 weeks
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'form': form, 'breadcrumb': breadcrumb})
    else:
        form = CustomUserAutorizationForm()
        return render(request, 'users/login.html', {'form': form, 'breadcrumb': breadcrumb})

def logout(request):
    auth_logout(request)
    return redirect('home')

def profile(request, user_id):
    breadcrumb = 'Profile'
    return render(request, 'users/profile.html', {'user_id': user_id, 'breadcrumb': breadcrumb})

def dashboard(request, user_id):
    user = Custom_user.objects.get(id=user_id)
    articles = Article.objects.filter(user=user_id)
    breadcrumb = 'Dashboard'
    return render(request, 'users/dashboard.html', {'user_id': user_id, 'breadcrumb': breadcrumb, 'user': user, 'articles': articles})

def settings(request, user_id):
    user = Custom_user.objects.get(id=user_id)
    breadcrumb = 'Settings'
    
    
    form = UserSettingsForm(instance=user)
       
    return render(request, 'users/settings.html', {'user_id': user_id, 'breadcrumb': breadcrumb, 'user': user, 'form': form})
    

def update_settings(request, user_id):
    user = Custom_user.objects.get(id=user_id)
    breadcrumb = 'Settings'
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=user)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.bio = form.cleaned_data['bio']
            user.specialization = form.cleaned_data['specialization']
            user.save()
            return redirect('dashboard', user_id=user_id)
        else:
            form = UserSettingsForm(instance=user)
            return render(request, 'users/settings.html', {'user_id': user_id, 'breadcrumb': breadcrumb, 'user': user, 'form': form})
    else:
        return redirect('settings', user_id=user_id)
    

def change_password(request, user_id):
    user = Custom_user.objects.get(id=user_id)
    breadcrumb = 'Settings'
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if user.check_password(current_password) :
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                request.session.set_expiry(1209600)  # 2 weeks
                return redirect('dashboard', user_id=user_id)
            else:
                error_message = "New passwords do not match."
        else:
            error_message = "Current password is incorrect."
        return render(request, 'users/settings.html', {'user_id': user_id, 'breadcrumb': breadcrumb, 'user': user, 'error_message': error_message})
    else:
        return redirect('settings', user_id=user_id)

def delete_account(request, user_id):
    user = Custom_user.objects.get(id=user_id)
    user.delete()
    return redirect('home')