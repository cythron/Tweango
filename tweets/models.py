from django.db import models


class Tweet(models.Model):
    content = models.TextField()
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.content[:10]
    