from django.db import models

class Calc(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    rate = models.FloatField()
    count = models.IntegerField()


class UserSong(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField()