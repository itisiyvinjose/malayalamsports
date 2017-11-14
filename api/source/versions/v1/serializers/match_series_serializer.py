from rest_framework import serializers
from api.models import MatchSeries


class MatchSeriesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MatchSeries
        fields = ('id', 'display_name', 'country', 'starting_date', 'ending_date', 'sport')