from django.db import models
from django.contrib.auth.models import User #built-in user model
import uuid

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver #this is for using decorators


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) #on_delete maintains one-to-one relationship
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True) #need pillow for this, which we already set up
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png") #in profiles folder in images folder
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    
    def __str__(self):
        return str(self.username) #wrapping it in str ensures it's a string in case username doesn't exist or is an integer or something


#@receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print('Profile Saved!')
    print('Instance:', instance)
    print('CREATED:', created)

def deleteUser(sender, instance, **kwargs):
    print('Deleting user...')

post_save.connect(profileUpdated, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)