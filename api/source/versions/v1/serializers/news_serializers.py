from django.db.models import Q
from rest_framework import serializers
from api.models import News, NewsRelationsShip


class NewsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'news_date', 'content', 'source', 'title', 'sport', 'is_trending', 'trend_scale', 'display_order', 'news_tags')




class NewsDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('news_date', 'content', 'source', 'title')

    @staticmethod
    def get_related_news(instance):
        related_news = NewsRelationsShip.objects.filter(news=instance).order_by('-relation_index').distinct()[:5]
        ordered_list = [relationship.related_news for relationship in related_news]
        # TODO: sort by relation_index
        return NewsListSerializer(ordered_list, many=True).data

    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'news_date': instance.news_date,
            'content': instance.content,
            'source': instance.source,
            'title': instance.title,
            'sport': instance.sport,
            'related_news': self.get_related_news(instance),
            'thumbnail_url': instance.thumbnail_image.url if instance.thumbnail_image else None,
            'image_url': instance.image.url if instance.image else None
        }
        return representation


class NewsListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'news_date', 'content', 'source', 'title')

    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'news_date': instance.news_date,
            'content': instance.content,
            'source': instance.source,
            'title': instance.title,
            'sport': instance.sport,
            'thumbnail_url': instance.thumbnail_image.url if instance.thumbnail_image else None,
            'image_url': instance.image.url if instance.image else None
        }
        return representation
