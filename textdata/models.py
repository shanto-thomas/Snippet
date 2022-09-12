from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)

class Snippet(models.Model):
    title = models.ForeignKey(Tag, related_name='tracks',on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(null=True)