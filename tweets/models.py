from django.db import models

import random

class Tweet(models.Model):
    content = models.TextField()
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.content[:10]
    
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0,150)
        }
    