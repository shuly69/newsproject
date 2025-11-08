from django.db import models
from django.utils.text import slugify
from user.models import CustomUser

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='articles', null=True, blank=True)
    excerpt = models.CharField(max_length=500, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, related_name='articles')
    subcategory = models.ForeignKey('SubCategories', on_delete=models.CASCADE, related_name='articles', null=True, blank=True)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    published_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title



class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # генерируем только если slug пустой
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name    



    
class SubCategories(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='subcategories')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # формируем slug с учётом категории, чтобы избежать коллизий
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name} ({self.category.name})"    