from django.db import models

class Groups(models.Model):
    GroupId = models.AutoField(primary_key=True)
    GroupName = models.CharField(max_length=20)
    PhotoFileName = models.CharField(max_length=100)


class Albums(models.Model):
    AlbumId = models.AutoField(primary_key=True)
    AlbumName = models.CharField(max_length=25)
    Group = models.CharField(max_length=25)
    DateAdded = models.DateField()
    PhotoFileName = models.CharField(max_length=100)