from django.contrib.auth.models import User
from django.db import models

class Song(models.Model):
    PRIVACY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
        ('protected', 'Protected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES)
    allowed_users = models.ManyToManyField(User, related_name='allowed_songs')


    def __str__(self):
        return self.title

