from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=256)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=250)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


from django.db import models

class Album(models.Model):
    artist = models.CharField (max_length=256)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)    
    album_logo = models.CharField(max_length=250)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)

    def __str__(self):
        return self.song_title + ' - ' + self.album.album_title
