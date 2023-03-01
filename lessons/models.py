from django.db import models

# Create your models here.

class Notes(models.Model):
    name = models.CharField(max_length=20)
    frequency = models.IntegerField()
    sound = models.FilePathField()
    image = models.FilePathField()

class Chords(models.Model):
    notes = models.JSONField()
    name = models.CharField(max_length=20)
    image = models.FilePathField()
    sound = models.FilePathField()

class Lessons(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/lessons_images/')
    finished = models.BooleanField(null=False, default=False)

    def __str__(self):
      return str(self.id) + ' - ' + self.title
    