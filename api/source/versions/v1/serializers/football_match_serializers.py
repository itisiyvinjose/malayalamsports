from rest_framework import serializers

from api.localisation import constants
from api.models import FootBallMatchDetails, FootballMatchCommentary, SportsTeam, MatchSeries, MatchPlayer
from api.source.versions.v1.serializers.football_commentary_serializers import FootballMatchCommentaryDetailsSerializer
from api.source.versions.v1.serializers.match_player_serializers import FootballMatchPlayerDetailsSerializer
from api.source.versions.v1.serializers.sports_team_serializers import SportsTeamDetailsSerializer


class FootBallMatchSerializer(serializers.ModelSerializer):
    """
    create football match record
    """
    team_one_id = serializers.IntegerField(required=True)
    team_two_id = serializers.IntegerField(required=True)
    match_starting_date = serializers.DateField(required=False, allow_null=True)
    match_starting_time = serializers.TimeField(required=False, allow_null=True)
    match_series_id = serializers.IntegerField(required=True)
    should_show_on_home_page = serializers.BooleanField(default=False, required=False)


    class Meta:
        model = FootBallMatchDetails
        fields = (
        'match_status', 'match_status_text', 'venue', 'match_starting_date', 'match_starting_time', 'team_one_id',
        'team_two_id', 'match_series_id', 'should_show_on_home_page')

    def validate_team_one_id(self, team_one_id):
        if SportsTeam.objects.filter(is_active=True, id=team_one_id, sport=constants.SPORTS_FOOTBALL).exists():
            return team_one_id
        else:
            message = 'Football team with id ' + str(team_one_id) + ' does not exists'
            raise serializers.ValidationError(message)


    def validate_team_two_id(self, team_two_id):
        if SportsTeam.objects.filter(is_active=True, id=team_two_id, sport=constants.SPORTS_FOOTBALL).exists():
            return team_two_id
        else:
            message = 'Football team with id ' + str(team_two_id) + ' does not exists'
            raise serializers.ValidationError(message)

    def validate_match_series_id(self, match_series_id):
        if MatchSeries.objects.filter(is_active=True, id=match_series_id, sport=constants.SPORTS_FOOTBALL).exists():
            return match_series_id
        else:
            message = 'Football match series with id ' + str(match_series_id) + ' does not exists'
            raise serializers.ValidationError(message)

    def validate(self, attrs):
        team_one_id = attrs['team_one_id']
        team_two_id = attrs['team_two_id']

        # check if ids are same
        if team_one_id == team_two_id:
            # raise error
            message = 'Both team_one_id and team_two_id are same'
            raise serializers.ValidationError(message)

        else:
            return attrs

    def create(self, validated_data):
        """
        create football match
        :param validated_data:
        :return:
        """
        football_match = FootBallMatchDetails()
        football_match.team_one_id = validated_data['team_one_id']
        football_match.team_two_id = validated_data['team_two_id']
        football_match.match_series_id = validated_data['match_series_id']
        football_match.match_status = validated_data['match_status']

        if 'match_starting_date' in validated_data:
            football_match.match_starting_time = validated_data['match_starting_date']

        if 'match_starting_date' in validated_data:
            football_match.match_starting_date = validated_data['match_starting_date']

        if 'match_status_text' in validated_data:
            football_match.match_status_text = validated_data['match_status_text']

        if 'should_show_on_home_page' in validated_data:
            football_match.should_show_on_home_page = validated_data['should_show_on_home_page']

        football_match.venue = validated_data['venue']

        football_match.save()
        return football_match

    def to_representation(self, instance):
        return FootBallMatchListSerializer(instance).data


class FootBallMatchUpdateSerializer(serializers.ModelSerializer):
    """
       update football match record
       """
    match_starting_date = serializers.DateField(required=False, allow_null=True)
    match_starting_time = serializers.TimeField(required=False, allow_null=True)
    match_finishing_date = serializers.DateField(required=False, allow_null=True)
    match_finishing_time = serializers.TimeField(required=False, allow_null=True)
    team_one_score = serializers.IntegerField(required=False, allow_null=True),
    team_two_score = serializers.IntegerField(required=False, allow_null=True)
    should_show_on_home_page = serializers.BooleanField(default=False, required=False)
    venue = serializers.CharField(max_length=200, required=False, allow_null=True)

    class Meta:
        model = FootBallMatchDetails
        fields = (
        'match_status', 'match_status_text', 'venue', 'match_starting_date', 'match_starting_time', 'team_one_score',
        'team_two_score', 'should_show_on_home_page', 'match_finishing_date', 'match_finishing_time')

    def update(self, instance, validated_data):
        instance.match_starting_date = validated_data.get('match_starting_date', instance.match_starting_date)
        instance.match_starting_time = validated_data.get('match_starting_time', instance.match_starting_time)
        instance.match_finishing_date = validated_data.get('match_finishing_date', instance.match_finishing_date)
        instance.match_finishing_time = validated_data.get('match_finishing_time', instance.match_finishing_time)
        instance.team_one_score = validated_data.get('team_one_score', instance.team_one_score)
        instance.team_two_score = validated_data.get('team_two_score', instance.team_two_score)
        instance.match_status = validated_data.get('match_status', instance.match_status)
        instance.match_status_text = validated_data.get('match_status_text', instance.match_status_text)
        instance.venue = validated_data.get('venue', instance.venue)
        instance.should_show_on_home_page = validated_data.get('should_show_on_home_page', instance.should_show_on_home_page)
        instance.save()
        return instance

    def to_representation(self, instance):
        return FootBallMatchListSerializer(instance).data



class FootBallMatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootBallMatchDetails

    @staticmethod
    def get_team_data(instance):
        return SportsTeamDetailsSerializer(instance).data

    def to_representation(self, instance):
        representation = {
            'match_id': instance.id,
            'match_status': instance.match_status,
            'match_status_text': instance.match_status_text,
            'match_series_name': instance.match_series.display_name,
            'venue': instance.venue,
            'match_starting_date': instance.match_starting_date,
            'match_starting_time': instance.match_starting_time,
            'team_one': self.get_team_data(instance.team_one),
            'team_two': self.get_team_data(instance.team_two),
            'team_one_score': instance.team_one_score,
            'team_two_score': instance.team_two_score,
            'should_show_on_home_page': instance.should_show_on_home_page
        }
        return representation


class FootBallMatchDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FootBallMatchDetails

    @staticmethod
    def get_team_data(instance):
        return SportsTeamDetailsSerializer(instance).data

    @staticmethod
    def get_players_list(instance):
        players = MatchPlayer.objects.filter(is_active=True, match=instance)
        return FootballMatchPlayerDetailsSerializer(players, many=True).data

    @staticmethod
    def get_live_comments(instance):
        commentaries = instance.commentaries.all().order_by('-created_at')[0:10]
        return FootballMatchCommentaryDetailsSerializer(commentaries, many=True).data

    def to_representation(self, instance):
        representation = {
            'match_id': instance.id,
            'match_status': instance.match_status,
            'match_status_text': instance.match_status_text,
            'match_series_name': instance.match_series.display_name,
            'venue': instance.venue,
            'match_starting_date': instance.match_starting_date,
            'match_starting_time': instance.match_starting_time,
            'team_one': self.get_team_data(instance.team_one),
            'team_two': self.get_team_data(instance.team_two),
            'team_one_score': instance.team_one_score,
            'team_two_score': instance.team_two_score,
            'should_show_on_home_page': instance.should_show_on_home_page,
            'commentaries': self.get_live_comments(instance),
            'players': self.get_players_list(instance)
        }
        return representation


class FootBallMatchLiveScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootBallMatchDetails

    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'team_one_score': instance.team_one_score,
            'team_two_score': instance.team_two_score,
            'match_status': instance.match_status,
            'match_status_text': instance.match_status_text,
        }
        return representation


class FootBallMatchLiveScoreCommentaryDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FootBallMatchDetails

    @staticmethod
    def get_live_comments(instance):
        commentaries = instance.commentaries.all().order_by('-created_at')[0:10]
        return FootballMatchCommentaryDetailsSerializer(commentaries, many=True).data


    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'team_one_score': instance.team_one_score,
            'team_two_score': instance.team_two_score,
            'match_status': instance.match_status,
            'match_status_text': instance.match_status_text,
            'commentaries': self.get_live_comments(instance)
        }
        return representation
