from django.db import models

# Create your models here.
class Bodypart(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    benefits = models.TextField(max_length=500)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']