from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Post


def post_list(request):
    return render(request,'im_blog/post_list.html',{})

def create(request):
    blog = Post()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def detail(request, blog_id):
    blog_detail = get_object_or_404(Post, pk=blog_id)
    return render(request, 'im_blog/detail.html', {'blog': blog_detail})