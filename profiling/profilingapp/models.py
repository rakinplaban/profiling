from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    father_name = models.CharField(max_length=100)
    address = models.TextField()
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name