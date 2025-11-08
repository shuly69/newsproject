from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('dashboard/<int:user_id>/', views.dashboard, name='dashboard'),
    path('settings/<int:user_id>/', views.settings, name='settings'),
    path('update_settings/<int:user_id>/', views.update_settings, name='update_settings'),
    path('change_password/<int:user_id>/', views.change_password, name='change_password'),
    path('delete_account/<int:user_id>/', views.delete_account, name='delete_account'),
]