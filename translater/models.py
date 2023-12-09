from django.db import models
from django.utils import timezone
import datetime

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)