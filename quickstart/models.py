from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
