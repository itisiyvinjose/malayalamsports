from django.conf.urls import url

from api.source.versions.v1.views.common.common_views import get_trending_news

urlpatterns = [
    url(r'^news/trending/list/$', get_trending_news, name='get_trending_news'),

]