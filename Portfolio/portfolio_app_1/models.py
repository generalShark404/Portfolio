from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    Technologies = models.CharField(max_length=250)
    features = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_created=True)
    source_code = models.URLField(null=True, blank=True)
    imgs = models.ImageField(upload_to='')