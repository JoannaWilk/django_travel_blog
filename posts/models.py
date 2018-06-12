from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def format_publish_date(self):
        return self.publish_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:103] + "..."

    def __str__(self):
        return self.title
