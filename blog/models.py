from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='carousel_img/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
    
class HeroList(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='hero_media/', blank=True, null=True)
    video = models.FileField(upload_to='hero_media/', blank=True, null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    main_hero = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_media/',blank=True, null=True)

    def __str__(self):
        return self.title