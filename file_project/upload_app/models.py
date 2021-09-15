from django.db import models


class wimag(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')
    Hex=models.CharField(max_length=32)

    def __str__(self):
        return self.title