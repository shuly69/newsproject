from django.contrib import admin
from .models import Articles, Categories, SubCategories
from .forms import ArticleForm

         



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug')
    search_fields = ['name']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'published_date', 'slug')


    form = ArticleForm
    class Media:
         css = {
            'all': ['https://cdn.quilljs.com/1.3.6/quill.snow.css', 'news/css/admin-editor.css']
                }
         js = ['https://cdn.quilljs.com/1.3.6/quill.js', 'news/js/editor.js', 'news/js/admin-subcategory.js']
         

   

admin.site.register(Categories, CategoryAdmin)
admin.site.register(SubCategories, SubCategoryAdmin)
admin.site.register(Articles, ArticleAdmin)
# Register your models here.

