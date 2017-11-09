from api.helpers import utils
from api.localisation import constants
from api.source.versions.v1.managers.data_managers import news_data_manager
from api.source.versions.v1.managers.data_managers.relationship_manager import RelationshipManager
from api.source.versions.v1.serializers.news_serializers import *
from api.source.versions.v1.services.base_service import *

def get_trending_news_service(request, params, user_agent):
    """
    filter trending news
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: list of news objects
    """
    data = news_data_manager.get_trending_news()
    return result(status=True, message=None, data=data, type=None)


def get_news_detail_service(request, params, user_agent):
    expected_params = [
        {'name': 'news_id', 'required': True, 'type': int, 'model': News,},
    ]
    validation = utils.validate_request(request_params=params, expected_params=expected_params)
    if validation.valid:

        news_id = params['news_id']
        news = News.objects.get(id=news_id)

        data = NewsDetailsSerializer(news).data
        RelationshipManager(news=news, tags=[])
        return result(status=True, message=None, data=data, type=None)
    else:
        message = validation.errors
        return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)

