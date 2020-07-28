from django.shortcuts import render, redirect, get_object_or_404
from .models import Post 

def new(request):
    return render(request, 'posts/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        user = request.user
        Post.objects.create(title=title, content=content, user = user, image = image)
    return redirect('posts:main')

def main(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html', {'posts':posts})

def show(request, id):
    post = Post.objects.get(pk=id)
    A = post.view_count
    A = A + 1
    post.view_count = A
    post.save() 
    return render(request, 'posts/show.html', {'post': post})

def update(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('posts:main')
    return render(request,'posts/update.html',{"post":post})

def delete(request,id):
    post=get_object_or_404(Post,pk=id)
    post.delete()
    return redirect("posts:main")
