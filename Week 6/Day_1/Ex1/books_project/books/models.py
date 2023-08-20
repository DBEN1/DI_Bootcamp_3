from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=200, blank=False)
    published_date = models.DateField(blank=False)
    description = models.TextField(blank=False)
    page_count = models.PositiveIntegerField()
    categories = models.CharField(max_length=200, blank=False)
    thumbnail_url = models.URLField(blank=True)  # This is optional, so blank=True
   
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField(blank=False, validators=[MinValueValidator(10)])


