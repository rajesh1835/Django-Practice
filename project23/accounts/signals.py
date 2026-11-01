import os

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, Profile
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def registartion_mail(sender,instance,created,**kwargs):
    if created:
        send_mail("Welcome On boarding ",
                              "You have Successfully registered 🎉",
                              "rajeshtarigonda@gmail.com",
                              [instance.email],
                              fail_silently=False)


@receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    if instance.profile:
        file_path = instance.profile.path

        os.remove(file_path)