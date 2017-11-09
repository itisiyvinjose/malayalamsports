from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import  News


@receiver(post_save, sender=News)
def post_save_news(sender, created, instance, **kwargs):

    # if newly created client, then add all super admins as users and admins to the client
    return
