from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()

class PortfolioElement(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='elements')
    content = RichTextField()
    media = models.ImageField(upload_to='media/', blank=True, null=True)
    order = models.IntegerField(default=0)
    font = models.CharField(max_length=50, default='Arial')
    color = models.CharField(max_length=7, default='#000000')  # Hex color code
