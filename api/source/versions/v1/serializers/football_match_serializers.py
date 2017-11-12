from rest_framework import serializers
from api.models import FootBallMatchDetails, FootballMatchCommentary
from api.source.versions.v1.serializers.sports_team_serializers import SportsTeamDetailsSerializer


# class FootBallMatchSerializer(serializers.ModelSerializer):



class FootBallMatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = FootBallMatchDetails

    @staticmethod
    def get_team_data(instance):
        return SportsTeamDetailsSerializer(instance).data

    def to_representation(self, instance):
        representation = {
            'match_id': instance.id,
            'match_status': instance.status,
            'status_text': instance.current_play_time_status,
            'venue': instance.venue,
            'match_title': instance.match_title,
            'match_starting_date': instance.match_starting_date,
            'match_starting_time': instance.match_starting_time,
            'team_one': self.get_team_data(instance.team_one),
            'team_two': self.get_team_data(instance.team_two),
            'team_one_score': instance.team_one_score,
            'team_two_score': instance.team_two_score,
        }
        return representation


class FootBallMatchScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = FootBallMatchDetails

    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'team_one_score': instance.team_one_score,
            'team_two_score': instance.team_two_score,
            'match_status': instance.status,
            'current_time_status': instance.current_play_time_status,
            'current_status_description': instance.current_status_text,
        }
        return representation



