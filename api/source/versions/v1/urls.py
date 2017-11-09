from django.conf.urls import url

from api.source.versions.v1.views.common.common_views import *

urlpatterns = [
    url(r'^news/trending/list/$', get_trending_news, name='get_trending_news'),
    url(r'^news/details/$', get_news_details, name='get_news_details'),

    url(r'^homepage/contents/$', get_home_page_contents, name='get_home_page_contents'),

]