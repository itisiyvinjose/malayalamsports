from api.helpers import utils
from api.localisation import constants
from api.models import MatchSeries
from api.source.versions.v1.managers.data_managers import news_data_manager
from api.source.versions.v1.managers.data_managers.relationship_manager import RelationshipManager
from api.source.versions.v1.serializers.match_series_serializer import MatchSeriesSerializer
from api.source.versions.v1.serializers.news_serializers import *
from api.source.versions.v1.services.base_service import *


def get_match_series_service(request, params, user_agent):
    expected_params = [
        {'name': 'sport', 'required': True, 'type': str},
    ]
    validation = utils.validate_request(request_params=params, expected_params=expected_params)
    if validation.valid:
        if params['sport'] == 'FOOTBALL':
            series = MatchSeries.objects.filter(is_active=True, sport=constants.SPORTS_FOOTBALL).all()
            data = MatchSeriesSerializer(series, many=True).data
            return result(status=True, message=None, data=data, type=None)
        else:
            message = "Not a valid sport"
    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def upload_match_series_logo_image_service(request, params, user_agent):

    if 'series_id' in params:
        series_id = int(params['series_id'])
        try:
            series = MatchSeries.objects.get(id=series_id)
            if 'image' in request.FILES and request.FILES['image']:
                image = request.FILES['image']
                series.logo_image = image
                series.save()
                data = MatchSeriesSerializer(series).data
                return result(status=True, message=None, data=data, type=None)
            else:
                message = '\'image\' field is required'

        except MatchSeries.DoesNotExist:
            message = 'MatchSeries with id ' + str(series_id) + ' does not exist'
    else:
        message = {
            "series_id": [
                "This field is required"
            ]
        }

    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)