from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    avatar_url = models.URLField()
    artist_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
class Track(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    cover_url = models.URLField()
    track_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name