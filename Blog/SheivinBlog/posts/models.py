from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    publishDate = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def publishDateFormat(self):
        return self.publishDate.strftime('%b %e %Y')

    def bodyFormat(self):
        return self.body[:100]