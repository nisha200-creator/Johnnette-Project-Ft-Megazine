from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name= models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self . category_name



STATUS_CHOICE =(
 ('default', 'draft'),
 ('published', 'published')
)

class Megazine(models.Model):
    
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)

    magazine_img = models.ImageField(upload_to='uploads/%y/%m/%d')
    short_desc = models.CharField(max_length=300)
    magazine_body = models.TextField(default="No content available")

    status = models.CharField(max_length=50,choices=STATUS_CHOICE, default='draft')
    is_featured = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    






class Crd(models.Model):
    title = models.CharField(max_length=255)
    short_desc = models.TextField(blank=True, null=True)  
    image = models.ImageField(upload_to='must_reads/images/')
    link = models.URLField()
    updated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title




    class Meta:
      verbose_name_plural = "Cards"





class FeaturedPost(models.Model):
    CATEGORY_CHOICES = [
        ('world', 'World'),
        ('business', 'Business'),
        ('technology', 'Technology'),
        ('sports', 'Sports'),
        ('health', 'Health'),
        ('entertainment', 'Entertainment'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='world')
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to='featured_posts/images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
# Create your models here.






class LeftContent(models.Model):
    
    title = models.CharField(max_length=255)
    short_desc = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    link = models.URLField(blank=True, null=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title