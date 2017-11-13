from api.helpers import utils
from api.localisation import constants
from api.source.versions.v1.managers.data_managers import news_data_manager
from api.source.versions.v1.managers.data_managers.relationship_manager import RelationshipManager
from api.source.versions.v1.serializers.news_serializers import *
from api.source.versions.v1.services.base_service import *


def add_news_service(request, params, user_agent):
    """
    filter trending news
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: list of news objects
    """
    serializer = NewsSerializer(data=params, context={'request': request})
    if not serializer.is_valid():
        return result(status=False, message=serializer.errors, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)

    serializer.save()
    return result(status=True, message=None, data=serializer.data, type=None)


def update_news_service(request, params, user_agent):
    """
    filter trending news
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: list of news objects
    """
    expected_params = [
        {'name': 'news_id', 'required': True, 'type': int, 'model': News, },
    ]
    validation = utils.validate_request(request_params=params, expected_params=expected_params)
    if validation.valid:

        news_id = params['news_id']
        news = News.objects.get(id=news_id)
        serializer = NewsSerializer(news, data=params, context={'request': request})

        if not serializer.is_valid():
            return result(status=False, message=serializer.errors, data=None,
                          type=constants.ERROR_RESPONSE_KEY_VALIDATION)

        serializer.save()
        return result(status=True, message=None, data=serializer.data, type=None)
    else:
        message = validation.errors
        return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def delete_news_service(request, params, user_agent):
    """
    filter trending news
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: list of news objects
    """
    expected_params = [
        {'name': 'news_id', 'required': True, 'type': int, 'model': News, },
    ]
    validation = utils.validate_request(request_params=params, expected_params=expected_params)
    if validation.valid:

        news_id = params['news_id']
        news = News.objects.get(id=news_id)
        news.delete()
        return result(status=True, message=None, data=None, type=None)
    else:
        message = validation.errors
        return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def list_news_service(request, params, user_agent):
    """
    filter trending news
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: list of news objects
    """
    expected_params = [
        {'name': 'offset', 'required': True, 'type': int, },
        {'name': 'limit', 'required': True, 'type': int, },

    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        offset = params['offset']
        limit = params['limit']

        news = News.objects.filter(is_active=True).order_by('-display_order')[offset:limit]
        data = NewsListSerializer(news, many=True).data
        total_count = News.objects.filter(is_active=True).count()
        response = {
            "content": data,
            "total_count": total_count
        }
        return result(status=True, message=None, data=response, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def get_news_details_service(request, params, user_agent):
    """
    filter trending news
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: list of news objects
    """
    expected_params = [
        {'name': 'news_id', 'required': True, 'type': int, 'model': News, },
    ]
    validation = utils.validate_request(request_params=params, expected_params=expected_params)
    if validation.valid:

        news_id = params['news_id']
        news = News.objects.get(id=news_id)
        data = NewsDetailsSerializer(news).data
        return result(status=True, message=None, data=data, type=None)
    else:
        message = validation.errors
        return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def get_trending_news_service(request, params, user_agent):
    """
    filter trending news
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: list of news objects
    """

    news = News.objects.filter(is_active=True, is_trending=True).order_by('-trend_scale')
    data = NewsListSerializer(news, many=True).data
    return result(status=True, message=None, data=data, type=None)
