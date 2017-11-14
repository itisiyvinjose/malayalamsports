from api.helpers import utils
from api.localisation import constants
from api.models import MatchSeries, SportsTeam
from api.source.versions.v1.managers.data_managers import news_data_manager
from api.source.versions.v1.managers.data_managers.relationship_manager import RelationshipManager
from api.source.versions.v1.serializers.news_serializers import *
from api.source.versions.v1.serializers.sports_team_serializers import SportsTeamListSerializer
from api.source.versions.v1.services.base_service import *


def get_teams_service(request, params, user_agent):
    expected_params = [
        {'name': 'sport', 'required': True, 'type': str, },
    ]
    validation = utils.validate_request(request_params=params, expected_params=expected_params)
    if validation.valid:
        if params['sport'] == 'FOOTBALL':
            teams = SportsTeam.objects.filter(is_active=True).all()
            data = SportsTeamListSerializer(teams, many=True).data
            return result(status=True, message=None, data=data, type=None)
        else:
            message = "Not a valid sport"
    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)
