from api.localisation import constants
from api.models import News
from api.source.versions.v1.serializers.news_serializers import NewsListSerializer
from api.source.versions.v1.services.base_service import *

def get_trending_news_service(request, params, user_agent):
    """
    filter trending news
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: list of news objects
    """
    number_of_news = constants.NUMBER_OF_TRENDING_NEWS
    trending_news = News.objects.filter(is_active=True, is_trending=True).order_by('trend_scale')[:number_of_news]
    data = NewsListSerializer(trending_news, many=True).data
    return result(status=True, message=None, data=data, type=None)

def get_news_detail_service():
    return