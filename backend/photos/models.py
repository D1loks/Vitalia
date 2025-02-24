from django.db import models


class Photo(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image_base64 = models.TextField()

    def __str__(self):
        return self.name
