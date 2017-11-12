
from rest_framework import serializers
from api.models import GuestNews


class GuestNewsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GuestNews
        fields = ('id', 'news_date', 'content', 'source', 'title', 'sport',)


class GuestNewsUpdateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GuestNews
        fields = ('id', 'news_date', 'content', 'source', 'title', 'sport', 'display_order', 'is_admin_approved')


class GuestNewsDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuestNews
        fields = ('news_date', 'content', 'source', 'title')


    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'news_date': instance.news_date,
            'content': instance.content,
            'source': instance.source,
            'title': instance.title,
            'sport': instance.sport
        }
        return representation


class GuestNewsListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GuestNews
        fields = ('id', 'news_date', 'content', 'source', 'title')
