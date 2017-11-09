from api.localisation import constants
from api.models import News, NewsTags
from api.source.versions.v1.serializers.news_serializers import *


def get_trending_news(exclude_news_ids=list()):
    number_of_news = constants.NUMBER_OF_TRENDING_NEWS
    trending_news = News.objects.filter(is_active=True, is_trending=True).exclude(id__in=exclude_news_ids).order_by(
        'trend_scale')[:number_of_news]
    data = NewsListSerializer(trending_news, many=True).data
    return data


def get_home_page_news():
    news = list()

    if News.objects.exists():

        number_of_news = constants.NUMBER_OF_NEWS_DISPLAYED_IN_WEB_HOME_PAGE
        homepage_news = News.objects.filter(is_active=True, should_display_on_home_page=True).order_by(
            'home_page_display_order')[:number_of_news]

        if homepage_news.count() > 0:
            news.extend(list(homepage_news))

        if len(news) < number_of_news:

            trending_news = News.objects.filter(is_active=True, is_trending=True).order_by('trend_scale')[
                            :number_of_news]
            if trending_news.count() > 0:
                news.extend(list(trending_news))

        if len(news) < number_of_news:

            all_news = News.objects.filter(is_active=True).order_by('news_date')[:number_of_news]
            if all_news.count() > 0:
                news.extend(list(all_news))

    data = NewsListSerializer(news, many=True).data
    return data
    #

