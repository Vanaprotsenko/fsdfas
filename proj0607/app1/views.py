from django.shortcuts import render
from .models import Post
from .models import Comment


def create_post(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        post = request.POST.get('post')
        if Post.objects.create(post=post,name=name):
            context['well'] = 'Ваш коментарь записан'
        else:
            context['bad'] = 'Сталась помилка'
    return render(request, 'app1/create_post.html',context)


def look_posts(request):
    comment = Comment.objects.all()
    post = Post.objects.all()

    
    context = {
        'post': post,
        'comment': comment
       }
    return render(request, 'app1/look_post.html', context)


def create_comment(request):
    context = {}
    if request.method == 'POST':
        comment = request.POST.get('comment')
        post = Post.objects.get(id = 1)
        comments = Comment.objects.create(comment=comment,post = post)
        context = {
            'comment': comments
        }
    return render (request, 'app1/create_com.html', context)






