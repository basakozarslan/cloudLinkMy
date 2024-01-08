"""from django.db import models

# Create your models here.

class ShortenedURL(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)"""

from django.db import models

class ShortenedURL(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Add a field for creation timestamp

    def __str__(self):
        return f"{self.short_code} - {self.long_url}"
