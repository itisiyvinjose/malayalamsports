from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import  News, FootBallMatchDetails
from api.source.versions.v1.managers.data_managers.relationship_manager import RelationshipManager


@receiver(post_save, sender=News)
def post_save_news(sender, created, instance, **kwargs):

    # print('finding and updating news relationship')
    if instance.news_tags and len(instance.news_tags) > 0:
        RelationshipManager(news=instance).find_and_update_news_relationship()


@receiver(post_save, sender=FootBallMatchDetails)
def post_save_news(sender, created, instance, **kwargs):

    # print('finding and updating news relationship')
    if instance.should_show_on_home_page:
        other_matches = FootBallMatchDetails.objects.filter(should_show_on_home_page=True).exclude(id=instance.id).all()
        for match in other_matches:
            match.should_show_on_home_page = False
            match.save()

