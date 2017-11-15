from rest_framework import serializers
from api.models import SportsTeam


class SportsTeamDetailsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SportsTeam
        fields = ('id', 'display_name')

    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'display_name': instance.display_name,
            'logo_image_url': instance.logo_image.url if instance.logo_image else None
        }
        return representation


class SportsTeamListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SportsTeam
        fields = ('id', 'display_name')

    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'display_name': instance.display_name,
            'logo_image_url': instance.logo_image.url if instance.logo_image else None
        }
        return representation
