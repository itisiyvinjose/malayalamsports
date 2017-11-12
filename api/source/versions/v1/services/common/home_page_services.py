from api.source.versions.v1.managers.data_managers import news_data_manager
from api.source.versions.v1.managers.data_managers import football_match_data_manager
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
    data['top_news'] = news_data_manager.get_home_page_news()
    data['trending_news'] = news_data_manager.get_trending_news()
    data['top_matches'] = football_match_data_manager.get_matches_to_be_displayed_on_home_page()
    data['kerala_blasters_top_matches'] = football_match_data_manager.get_kerala_blasters_matches_to_be_displayed_on_home_page()

    return result(status=True, message=None, data=data, type=None)






