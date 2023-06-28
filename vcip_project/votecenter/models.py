from django.db import models

class VoteCenter(models.Model):
    sitename = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='votecenter/images/')
    url = models.URLField(blank=True)

# Create your models here.
