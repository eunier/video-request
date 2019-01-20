from django.db import models
from django.utils import timezone


# Create your models here.
class Video(models.Model):
    video_title = models.CharField(max_length=20)
    video_desc = models.TextField()
    date_added = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.video_title, self.id)

