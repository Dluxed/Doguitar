from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=25, null = False, blank = False)
    user_email = models.EmailField(null=True)
    #user_image = models.FilePathField()
    level = models.IntegerField()
    
