from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.postgres.search import SearchVector
from .forms import ArticleForm
from .models import Articles, Categories
from user.models import CustomUser
from django.core.paginator import Paginator
# Create your views here.
def get_articles(request):
    all_news = Articles.objects.all().order_by('-published_date')
    main_news = all_news.first() if all_news else None
    sides_news = all_news[1:3] if all_news.count() > 2 else all_news[1:] if all_news.count() > 1 else []
    other_news = all_news[3:9] if all_news.count() > 3 else []
    context = {
        'main_news': main_news,
        'sides_news': sides_news,
        'other_news': other_news,
    }
    return render(request, 'articles/main.html', context)

def get_article(request, slug):
    breadcrumb = slug.replace('-', ' ').title()
    article = get_object_or_404(Articles, slug=slug)
    user = CustomUser.objects.get(id=article.user_id)
    return render(request, 'articles/article.html', {'article': article, 'user': user, 'breadcrumb': breadcrumb})

def update_article(request, article_id):
    breadcrumb = 'Update Article'
    article = get_object_or_404(Articles, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)   # пока не сохраняем в БД
            article.user = request.user         # привязываем текущего пользователя


            form.save()
            return redirect('home')
        else:
            return render(request, 'articles/update.html', {'form': form, 'breadcrumb': breadcrumb, 'article_id': article_id})
    else:
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'breadcrumb': breadcrumb, 'article_id': article_id})


def get_category(request, slug):
    breadcrumb = slug.replace('-', ' ').title()
    date_filter = '-published_date'
    category = Categories.objects.get(slug=slug)
    articles = Articles.objects.filter(category=category).order_by(date_filter) 
    if request.GET.get('date') == 'oldest' :
        date_filter = 'published_date'
        articles = Articles.objects.filter(category=category).order_by(date_filter)
    if request.GET.get('subcategory') and request.GET.get('subcategory') != 'all':
        subcategory_id = request.GET.get('subcategory')
        articles = Articles.objects.filter(subcategory__id=subcategory_id ).order_by(date_filter)  
  

    
    categories = ['news', 'technology', 'sport', 'lifestyle', 'business', 'culture']
    main_article = articles.first() if articles else None
    lastest_articles = articles[1:]  if articles.count() > 1 else []
    
    paginator = Paginator(lastest_articles, 6)  # Show 5 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    subcategorys = category.subcategories.all()
    return render(request, 'articles/category.html', {'category': category, 'articles': articles , 'main_article': main_article, 'page_obj': page_obj, 'lastest_articles': lastest_articles, 'subcategorys': subcategorys ,  'categories': categories, 'breadcrumb': breadcrumb})

def search_articles(request):
    breadcrumb = 'Search Results'
    query = request.GET.get('search', 0)
    results = Articles.objects.all()
    if query:
        results = Articles.objects.annotate(
            search=SearchVector('title', 'content', 'excerpt'),
        ).filter(search=query)
    return render(request, 'articles/search.html', {'results': results, 'query': query, 'breadcrumb': breadcrumb})


def create_article(request):
    breadcrumb = 'Create Article'
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        
        if form.is_valid():
            article = form.save(commit=False)   # пока не сохраняем в БД
            article.user = request.user         # привязываем текущего пользователя


            form.save()
            return redirect('home')
        else:
           
            return render(request, 'articles/create.html', {'form': form, 'breadcrumb': breadcrumb})
    else:
        form = ArticleForm()

        return render(request, 'articles/create.html', {'form': form, 'breadcrumb': breadcrumb})
    
def delete_article(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    user = request.user
    if article.user != user:
        return redirect('home')  # Или вернуть ошибку 403 Forbidden
    
    article.delete()
    
    return redirect('dashboard', user_id=user.id )