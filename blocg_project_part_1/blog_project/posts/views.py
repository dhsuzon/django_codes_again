
from django.shortcuts import render,redirect
from posts.forms import PostForm
from posts.models import Post


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return  redirect('homepage')
    else:
        form = PostForm()
    return render(request,'add_post.html', {'form': form})



def edit_post(request,id):
    post = Post.objects.get(pk=id)
    editPost = PostForm(instance=post)
    if request.method =="POST":
        editPost = PostForm(request.POST,instance=post)
        if editPost.is_valid():
            editPost.save()
            return redirect('homepage')
    return render(request,'add_post.html', {'form': editPost})



def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')