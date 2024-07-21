from django.db import models

# Create your models here.

class  Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    github = models.URLField()
    linkedIn = models.URLField(null=True, blank=True)
    x_twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

STATUS = (
    ('status', 'Live'),
    ('status', 'Not Hosted')
)

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    Technologies = models.CharField(max_length=250)
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_created=True)
    source_code = models.URLField(null=True, blank=True)
    thumbnail_img = models.ImageField(upload_to='project_imgs/', null=True)
    status = models.CharField(max_length=6, choices=STATUS, null=True)

    def __str__(self):
        return self.title

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_imgs/')

    def __str__(self):
        return f"{self.project.title} image"

class ProjectFeature(models.Model):
    header = models.CharField(max_length=150, blank=True, default="")
    project = models.ForeignKey(Project, related_name='feature', on_delete=models.CASCADE)
    feature = models.CharField(max_length=350)