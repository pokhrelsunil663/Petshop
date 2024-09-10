from django.db import models


class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/')
    content=models.TextField()
    author=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
