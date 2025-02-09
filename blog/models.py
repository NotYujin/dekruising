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
    
class ClientMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    company = models.CharField(max_length=100, blank=True, null=True, verbose_name="Company")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    message = models.TextField(verbose_name="Message")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Sent At")

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

    class Meta:
        verbose_name = "Client Message"
        verbose_name_plural = "Client Messages"
        ordering = ['-sent_at']