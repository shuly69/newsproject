from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# Create your models here.


    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=100, choices=[
        ('lifestyle', 'Lifestyle'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),
        ('Culture', 'Culture'),
        ('news', 'News'),
        ('business', 'Business'),
    ], blank=True, null=True)
    
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email