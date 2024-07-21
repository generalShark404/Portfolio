from django.db import models

# Create your models here.
class BlogCategory(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    blog_img = models.ImageField(upload_to="blog_imgs", null=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.title} - {self.category}" 