from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250, null='true')
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return '{}'.format(self.name)
