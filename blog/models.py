from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish_date')
    author = models.ForeignKey(User,
                               related_name='blog_posts',
                               on_delete=models.CASCADE)
    body = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title
