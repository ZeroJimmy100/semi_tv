from django.db import models
from datetime import datetime, date


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=15)
    description = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # release_date = models.DateField(auto_now_add=False, auto_now=False, blank =True)
    # timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)




# Create your models here.
