from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=25, null = False, blank = False)
    user_email = models.EmailField(null=True)
    #user_image = models.FilePathField()
    level = models.IntegerField()

    def __str__(self):
        return str(self.id) + ' - ' +self.username
    
class Lessons(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    finished = models.BooleanField(null=False, default=False)


    def __str__(self):
        return str(self.id) + ' - ' + self.title
    