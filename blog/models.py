from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# creating custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

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
    image = models.ImageField(upload_to='media/',
                              blank=True, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    # adding created PublishedManager
    objects = models.Manager() # default
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish_date.year,
                             self.publish_date.strftime('%m'),
                             self.publish_date.strftime('%d'),
                             self.slug])

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title
