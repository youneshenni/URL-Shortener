from django.db import models
from django.utils import timezone 
# Create your models here.
class MiniURL(models.Model):
    LongURL = models.URLField(unique=True, verbose_name="Long URL")
    code = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)
