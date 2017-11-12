from rest_framework import serializers
from api.models import MatchPlayer, FootBallMatchDetails


class FootballMatchPlayerSerializer(serializers.ModelSerializer):
    match_id = serializers.IntegerField(required=True, allow_null=False)

    class Meta:
        model = MatchPlayer
        fields = (
            'match_id', 'name', 'jersey_number', 'player_role', 'position', 'order')


    def validate_match_id(self, match_id):
        if FootBallMatchDetails.objects.filter(is_active=True, id=match_id).exists():
            return match_id
        else:
            raise serializers.ValidationError('Match with id ' + match_id + ' does not exists')

    def create(self, validated_data):
        instance = MatchPlayer()
        instance.match_id = validated_data['match_id']
        instance.name = validated_data['name']

        if 'jersey_number' in validated_data:
            instance.jersey_number = validated_data['jersey_number']

        if 'position' in validated_data:
            instance.position = validated_data['position']

        if 'player_role' in validated_data:
            instance.player_role = validated_data['player_role']

        instance.save()
        return instance

    def to_representation(self, instance):
        return FootballMatchPlayerDetailsSerializer(instance).data


class  FootballMatchPlayerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchPlayer
        fields = (
             'name', 'jersey_number', 'player_role', 'position', 'order')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.jersey_number = validated_data.get('jersey_number', instance.jersey_number)
        instance.player_role = validated_data.get('player_role', instance.player_role)
        instance.position = validated_data.get('position', instance.position)
        instance.save()
        return instance


    def to_representation(self, instance):
        return FootballMatchPlayerDetailsSerializer(instance, context=self.context).data

class FootballMatchPlayerDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchPlayer
        fields = (
            'id', 'name', 'jersey_number', 'player_role', 'position', 'order')