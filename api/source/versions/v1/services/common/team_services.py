import io
from PIL import Image
from io import StringIO
from django.core.files.base import ContentFile

from api.helpers import utils
from api.localisation import constants
from api.models import MatchSeries, SportsTeam
from api.source.versions.v1.managers.data_managers import news_data_manager
from api.source.versions.v1.managers.data_managers.relationship_manager import RelationshipManager
from api.source.versions.v1.serializers.news_serializers import *
from api.source.versions.v1.serializers.sports_team_serializers import SportsTeamListSerializer, \
    SportsTeamDetailsSerializer
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


def upload_team_logo_service(request, params, user_agent):

    if 'team_id' in params:
        team_id = int(params['team_id'])
        try:
            team = SportsTeam.objects.get(id=params['team_id'])
            if 'logo_image' in request.FILES:
                logo_image = request.FILES['logo_image']
                # im = Image.open(logo_image)
                #
                # image_w, image_h = im.size
                #
                # lmg_size = (100, 100)
                # resize_image = im.resize(lmg_size, Image.ANTIALIAS)
                # # resize_image.show()
                #
                # img_io = io.BytesIO()
                # resize_image.save(img_io, format='JPEG', quality=100)
                # img_content = ContentFile(img_io.getvalue(), 'img5.jpg')
                #
                # team.logo_image = img_content
                team.logo_image = logo_image
                team.save()
                data = SportsTeamDetailsSerializer(team).data
                return result(status=True, message=None, data=data, type=None)
            else:
                message = '\'logo_image\' field is required'

        except SportsTeam.DoesNotExist:
            message = 'SportTeam with id ' + str(team_id) + ' does not exist'
    else:
        message = {
            "team_id": [
                "This field is required"
            ]
        }

    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)
