from django.urls import path
from . import views

urlpatterns = [
     path('', views.get_articles, name='home'),
     path('article/<slug:slug>/', views.get_article, name='article_detail'),
     path('category/<slug:slug>/', views.get_category, name='category'),
     path('create/', views.create_article, name='create_article'),
     path('search/', views.search_articles, name='search_articles'),
     path('article/update/<int:article_id>/', views.update_article, name='update_article'),
     path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
]