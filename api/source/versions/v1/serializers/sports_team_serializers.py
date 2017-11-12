from rest_framework import serializers
from api.models import SportsTeam


class SportsTeamDetailsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SportsTeam
        fields = ('id', 'name')


class SportsTeamListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SportsTeam
        fields = ('id', 'name')
