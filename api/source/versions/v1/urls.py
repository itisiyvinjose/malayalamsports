from django.conf.urls import url
from api.source.versions.v1.views.admin_views import *
from api.source.versions.v1.views.common.common_views import *
from api.source.versions.v1.views.common.upload_views import *

urlpatterns = [

    url(r'^homepage/contents/$', get_home_page_contents, name='get_home_page_contents'),

    url(r'^match/football/create/$', create_football_match, name='create_football_match'),
    url(r'^match/football/update/$', update_football_match, name='update_football_match'),
    url(r'^match/football/delete/$', delete_football_match, name='delete_football_match'),
    url(r'^match/football/details/$', get_football_match_details, name='get_football_match_details'),
    url(r'^match/football/live/list/$', get_live_football_matches, name='get_live_football_matches'),
    url(r'^match/football/upcoming/list/$', get_upcoming_football_matches, name='get_upcoming_football_matches'),

    url(r'^match/football/commentary/add/$', add_football_match_commentary, name='add_football_match_commentary'),
    url(r'^match/football/commentary/update/$', update_football_match_commentary,
        name='update_football_match_commentary'),
    url(r'^match/football/commentary/delete/$', delete_football_match_commentary,
        name='delete_football_match_commentary'),
    url(r'^match/football/commentary/list/$', list_football_match_commentary, name='list_football_match_commentary'),

    url(r'^match/football/live/scores/$', get_live_football_scores, name='get_live_football_scores'),
    url(r'^match/football/live/scores_and_commentaries/$', get_live_football_scores_commentaries,
        name='get_live_football_scores_commentaries'),

    url(r'^match/football/player/add/$', add_football_match_player, name='add_football_match_player'),
    url(r'^match/football/player/update/$', update_football_match_player, name='update_football_match_player'),
    url(r'^match/football/player/delete/$', delete_football_match_player, name='delete_football_match_player'),
    url(r'^match/football/player/list/$', list_football_match_player, name='list_football_match_player'),

    url(r'^news/create/$', add_news, name='add_news'),
    url(r'^news/update/$', update_news, name='update_news'),
    url(r'^news/delete/$', delete_news, name='delete_news'),
    url(r'^news/details/$', get_news_details, name='get_news_details'),
    url(r'^news/trending/list/$', get_trending_news, name='get_trending_news'),
    url(r'^news/list/$', get_all_news, name='get_all_news'),

    url(r'^guest/news/create/$', add_guest_news, name='add_guest_news'),
    url(r'^guest/news/update/$', update_guest_news, name='update_guest_news'),
    url(r'^guest/news/delete/$', delete_guest_news, name='delete_guest_news'),
    url(r'^guest/news/details/$', guest_news_details, name='guest_news_details'),
    url(r'^guest/news/list/$', list_guest_news, name='list_guest_news'),

    url(r'^match_series/list/$', get_match_series_list, name='get_match_series_list'),
    url(r'^sport_team/list/$', get_teams_list, name='get_teams_list'),

    url(r'^sport_team/logo/$', upload_team_logo, name='upload_team_logo'),
    url(r'^news/image/$', upload_news_image, name='upload_news_image'),
    url(r'^guest_news/image/$', upload_guest_news_image, name='upload_guest_news_image'),

]
