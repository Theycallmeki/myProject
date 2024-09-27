from django.db import models
from django.contrib.auth.models import User  # Import the User model for linking portfolios to users
from ckeditor.fields import RichTextField

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolios', null=True)
    title = models.CharField(max_length=200)
    description = RichTextField()

    def __str__(self):
        return self.title

class PortfolioElement(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='elements')  # Link to Portfolio
    content = RichTextField()
    media = models.ImageField(upload_to='media/', blank=True, null=True)  # Optional media upload
    order = models.IntegerField(default=0)  # Order of elements in the portfolio
    font = models.CharField(max_length=50, default='Arial')  # Font for the element
    color = models.CharField(max_length=7, default='#000000')  # Hex color code for the element

    def __str__(self):
        return f"Element {self.order} in {self.portfolio.title}"
