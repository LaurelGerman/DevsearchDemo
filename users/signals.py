from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver #this is for using decorators

from django.contrib.auth.models import User #built-in user model
from .models import Profile

#@receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created: #created is boolean
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

def deleteUser(sender, instance, **kwargs):
    user=instance.user,
    user.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)