from api.helpers import utils
from api.localisation import constants
from api.source.versions.v1.managers.data_managers import news_data_manager
from api.source.versions.v1.managers.data_managers.relationship_manager import RelationshipManager
from api.source.versions.v1.serializers.guest_news_serializers import *
from api.source.versions.v1.serializers.news_serializers import *
from api.source.versions.v1.services.base_service import *


def add_guest_news_service(request, params, user_agent):
    """
    filter trending news
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: list of news objects
    """
    serializer = GuestNewsSerializer(data=params, context={'request': request})
    if not serializer.is_valid():
        return result(status=False, message=serializer.errors, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)

    serializer.save()
    return result(status=True, message=None, data=serializer.data, type=None)


def update_guest_news_service(request, params, user_agent):
    """
    filter trending news
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: list of news objects
    """
    expected_params = [
        {'name': 'news_id', 'required': True, 'type': int, 'model': GuestNews, },
    ]
    validation = utils.validate_request(request_params=params, expected_params=expected_params)
    if validation.valid:

        news_id = params['news_id']
        news = GuestNews.objects.get(id=news_id)
        serializer = GuestNewsUpdateSerializer(news, data=params, context={'request': request})

        if not serializer.is_valid():
            return result(status=False, message=serializer.errors, data=None,
                          type=constants.ERROR_RESPONSE_KEY_VALIDATION)

        serializer.save()
        return result(status=True, message=None, data=serializer.data, type=None)
    else:
        message = validation.errors
        return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def delete_guest_news_service(request, params, user_agent):
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
        news = GuestNews.objects.get(id=news_id)
        news.delete()
        return result(status=True, message=None, data=None, type=None)
    else:
        message = validation.errors
        return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def list_guest_news_service(request, params, user_agent):
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

        news = GuestNews.objects.filter(is_active=True).order_by('-created_at')[offset:limit]
        total_count = GuestNews.objects.filter(is_active=True).count()
        data = GuestNewsListSerializer(news, many=True).data
        response = {
            "content" : data,
            "total_count": total_count
        }

        return result(status=True, message=None, data=response, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def get_guest_news_details_service(request, params, user_agent):
    """
    filter trending news
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: list of news objects
    """
    expected_params = [
        {'name': 'news_id', 'required': True, 'type': int, 'model': GuestNews, },
    ]
    validation = utils.validate_request(request_params=params, expected_params=expected_params)
    if validation.valid:

        news_id = params['news_id']
        news = GuestNews.objects.get(id=news_id)
        data = GuestNewsDetailsSerializer(news).data
        return result(status=True, message=None, data=data, type=None)
    else:
        message = validation.errors
        return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)



def upload_guest_news_image_service(request, params, user_agent):

    if 'guest_news_id' in params:
        guest_news_id = int(params['guest_news_id'])
        try:
            news = GuestNews.objects.get(id=guest_news_id)
            if 'guest_news_image' in request.FILES and request.FILES['guest_news_image']:
                image = request.FILES['guest_news_image']
                news.image = image
                news.save()
                data = GuestNewsDetailsSerializer(news).data
                return result(status=True, message=None, data=data, type=None)
            else:
                message = '\'guest_news_image\' field is required'

        except News.DoesNotExist:
            message = 'Guest news with id ' + str(guest_news_id) + ' does not exist'
    else:
        message = {
            "guest_news_id": [
                "This field is required"
            ]
        }

    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)