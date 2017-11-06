from rest_framework import serializers
from api.models import SportTeam


class SportsTeamDetailsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SportTeam
        fields = ('id', 'name')


class SportsTeamListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SportTeam
        fields = ('id', 'name')
