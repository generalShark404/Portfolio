from django.urls import path
from .views import BlogPostsView, BlogDetailView

app_name = 'blog'
urlpatterns = [
    path('blogs', BlogPostsView, name="blog_posts"),
    path('blog-detail/<str:title>/<int:id>', BlogDetailView, name="blog-detail"),
]

