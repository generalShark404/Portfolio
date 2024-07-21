from django.shortcuts import render
from .models import BlogPost, BlogCategory

# Create your views here.
def BlogPostsView(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog.html', {'blogs':blogs})

def BlogDetailView(request, *arg, **kwargs):
    id = kwargs.get('id', None)
    blog = BlogPost.objects.get(id=id)
    return render(request, 'blog-detail.html', {'blog':blog})