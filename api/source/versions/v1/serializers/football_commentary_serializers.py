from rest_framework import serializers
from api.models import FootballMatchCommentary, FootBallMatchDetails, CommentaryTagImage


class FootballMatchCommentarySerializer(serializers.ModelSerializer):
    match_id = serializers.IntegerField(required=True, allow_null=False)

    class Meta:
        model = FootballMatchCommentary
        fields = (
            'match_id', 'commentary_heading', 'commentary_content', 'is_key_event', 'current_play_time_status', 'tag')

    def validate_match_id(self, match_id):
        if FootBallMatchDetails.objects.filter(is_active=True, id=match_id).exists():
            return match_id
        else:
            raise serializers.ValidationError('Match with id ' + str(match_id) + ' does not exists')

    def create(self, validated_data):
        instance = FootballMatchCommentary()
        instance.football_match_id = validated_data['match_id']
        instance.commentary_content = validated_data['commentary_content']

        if 'commentary_heading' in validated_data:
            instance.commentary_heading = validated_data['commentary_heading']

        if 'is_key_event' in validated_data:
            instance.is_key_event = validated_data['is_key_event']

        if 'current_play_time_status' in validated_data:
            instance.current_play_time_status = validated_data['current_play_time_status']

        if 'tag' in validated_data and validated_data['tag']:
            instance.tag = validated_data['tag']

        instance.save()
        return instance

    def to_representation(self, instance):
        return FootballMatchCommentaryDetailsSerializer(instance, context=self.context).data


class FootballMatchCommentaryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = FootballMatchCommentary
        fields = (
             'commentary_heading', 'commentary_content', 'is_key_event', 'current_play_time_status')

    def update(self, instance, validated_data):
        instance.commentary_heading = validated_data.get('commentary_heading', instance.commentary_heading)
        instance.is_key_event = validated_data.get('is_key_event', instance.is_key_event)
        instance.current_play_time_status = validated_data.get('current_play_time_status', instance.current_play_time_status)
        instance.commentary_content = validated_data.get('commentary_content', instance.commentary_content)
        instance.save()
        return instance


    def to_representation(self, instance):
        return FootballMatchCommentaryDetailsSerializer(instance, context=self.context).data


class FootballMatchCommentaryDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FootballMatchCommentary
        fields = (
            'id', 'commentary_heading', 'commentary_content', 'is_key_event', 'current_play_time_status',
            'football_match', 'created_at', 'tag')

    @staticmethod
    def get_tag_image(instance):
        if instance.tag:
            return CommentaryTagImage.objects.get(tag=instance.tag).image.url
        return None


    def to_representation(self, instance):

        representation = {
            'id': instance.id,
            'commentary_heading': instance.commentary_heading,
            'commentary_content': instance.commentary_content,
            'is_key_event': instance.is_key_event,
            'current_play_time_status': instance.current_play_time_status,
            'football_match': instance.football_match.id,
            'created_at': instance.created_at,
            'tag': instance.tag,
            'tag_image_url': self.get_tag_image(instance),
        }

        return representation
