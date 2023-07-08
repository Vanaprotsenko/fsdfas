from django.shortcuts import render
from .models import Post
from .models import Comment


def create_post(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        post = request.POST.get('post')
        if Post.objects.create(name=name, post=post):
            context['well'] = 'Ваш коментарь записан'
        else:
            context['bad'] = 'Сталась помилка'
    return render(request, 'app1/create_post.html',context)


def look_posts(request):
    comment = Comment.objects.all()
    posts =  Post.objects.all()
    context = {
        'posts': posts,
        'comment': comment
       }
    return render(request, 'app1/look_post.html', context)


def create_comment(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        text_of_comment = request.POST.get('text_of_comment')
        comment = request.POST.get('comment')
        if Post.objects.filter(name=name):
            Comment.objects.create(text_of_comment = text_of_comment,comment = comment)
        else:
            context['error'] = ''
    return render(request, 'app1/create_com.html', context)
       
