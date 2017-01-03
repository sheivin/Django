from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-publishDate')
    return render(request, 'posts/home.html', {'posts': posts})

def postFull(request, postId):
    post = get_object_or_404(Post, pk=postId)
    return render(request, 'posts/postFull.html', {'post': post})