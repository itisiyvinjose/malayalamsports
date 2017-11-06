from rest_framework import serializers
from api.models import News, NewsRelationsShip


class NewsDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('news_date', 'content', 'source', 'title')

    @staticmethod
    def get_related_news(instance):
        related_news = NewsRelationsShip.objects.filter(news=instance)
        ordered_list = list(related_news)
        # TODO: sort by relation_index
        return NewsListSerializer(ordered_list, many=True).data

    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'news_date': instance.news_date,
            'content': instance.content,
            'source': instance.source,
            'title': instance.title,
            'related_news': self.get_related_news(instance)
        }
        return representation


class NewsListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'news_date', 'content', 'source', 'title', 'thumbnail')
