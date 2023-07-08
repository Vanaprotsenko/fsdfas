from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=30)
    post = models.CharField(max_length=255)
    

    


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, null = True, blank=True)
    text_of_comment = models.CharField(max_length=255,null = True, blank = True)
    name = models.CharField(max_length=30,null = True, blank=True)
