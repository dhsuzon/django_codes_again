from django.shortcuts import render,redirect
from posts.models import Post



def Home(request):
    data = Post.objects.all()
    return render(request, 'home.html',{'data':data})