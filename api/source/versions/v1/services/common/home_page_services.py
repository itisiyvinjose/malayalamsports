from api.localisation import constants
from api.models import News, FootBallMatchDetails, GuestNews
from api.source.versions.v1.managers.data_managers import news_data_manager
from api.source.versions.v1.managers.data_managers import football_match_data_manager
from api.source.versions.v1.serializers.football_match_serializers import FootBallMatchListSerializer
from api.source.versions.v1.serializers.guest_news_serializers import GuestNewsListSerializer
from api.source.versions.v1.serializers.news_serializers import NewsListSerializer
from api.source.versions.v1.services.base_service import *


def get_home_page_contents_service(request, params, user_agent):
    """
    return contents to be shown in the home page of the web and mobile app
    ::param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """

    data = dict()

    # news
    data['news'] = dict()
    news = News.objects.filter(is_active=True).order_by('-display_order')[0:10]
    news_data = NewsListSerializer(news, many=True).data
    news_count = News.objects.filter(is_active=True).count()
    news_response = {
        "content": news_data,
        "total_count": news_count
    }
    data['news'] = news_response

    # trending news
    data['trending_news'] = dict()
    trending_news = News.objects.filter(is_active=True, is_trending=True).order_by('-trend_scale')
    trending_news_data = NewsListSerializer(trending_news, many=True).data
    data['trending_news'] = trending_news_data
    trending_news_count = News.objects.filter(is_active=True, is_trending=True).count()
    trending_news_response = {
        "content": trending_news_data,
        "total_count": trending_news_count
    }
    data['trending_news'] = trending_news_response

    data['guest_news'] = dict()
    guest_news = GuestNews.objects.filter(is_active=True).order_by('-created_at')[0:10]
    guest_news_total_count = GuestNews.objects.filter(is_active=True).count()
    guest_news_data = GuestNewsListSerializer(guest_news, many=True).data
    guest_news_response = {
        "content": guest_news_data,
        "total_count": guest_news_total_count
    }
    data['guest_news'] = guest_news_response

    # live matches
    data['live_matches'] = list()

    matches_should_be_displayed = FootBallMatchDetails.objects.filter(is_active=True,
                                                                      should_show_on_home_page=True).all()

    if matches_should_be_displayed.count() > 0:
        final_matches_list = [matches_should_be_displayed[0]]

    else:
        final_matches_list = []

    live_matches_data = FootBallMatchListSerializer(final_matches_list, many=True).data
    data['live_matches'] = live_matches_data

    # upcoming_matches
    data['upcoming_matches'] = list()

    matches_should_be_displayed = FootBallMatchDetails.objects.filter(is_active=True,
                                                                      match_status=constants.MATCH_STATUS_UPCOMING).order_by(
        'match_starting_date', 'match_starting_time').all()

    if matches_should_be_displayed.count() > 0:
        final_matches_list = [matches_should_be_displayed[0]]

    else:
        final_matches_list = []

    upcoming_matches_data = FootBallMatchListSerializer(final_matches_list, many=True).data
    data['upcoming_matches'] = upcoming_matches_data

    return result(status=True, message=None, data=data, type=None)






