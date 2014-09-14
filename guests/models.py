from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
