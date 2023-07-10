from django.db import models

class Post(models.Model):
    post = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


    
class Comment(models.Model):
    comment = models.CharField(max_length=255)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null= True)


# def create_comment(request):
#     context = {}
#     if request.method == 'POST':
#         comment = request.POST.get('comment')
#         post = Post.objects.get(id = 1)
#         comments = Comment.objects.create(comment=comment,post = post)
#         context = {
#             'comment': comments
#         }
#     return render (request, 'app/create_com.html', context)


# class Post(models.Model):
#     post = models.CharField(max_length=255)


    
# class Comment(models.Model):
#     comment = models.CharField(max_length=255)
#     post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null= True)
