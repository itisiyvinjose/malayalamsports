from rest_framework import serializers
from api.models import FootballMatchCommentary


class FootballMatchCommentaryDetailsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FootballMatchCommentary
        fields = ('id', 'current_play_time_status', 'added_time', 'comment')
