from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'posts/index.html', context)


def create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostModelForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)