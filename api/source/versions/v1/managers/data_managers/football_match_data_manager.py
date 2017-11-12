from datetime import datetime, date, timedelta
from api.localisation import constants
from api.models import FootBallMatchDetails, SportsTeam
from api.source.versions.v1.serializers.football_match_serializers import FootBallMatchListSerializer


def get_matches_to_be_displayed_on_home_page(exclude_ids=None):
    matches = FootBallMatchDetails.objects.filter(is_active=True, should_show_on_home_page=True, is_kerala_blasters_involved=False).order_by('display_priority_scale')
    matches = list(matches)
    # filtered_matches = list()

    # remove kerala blasters
    # for match in matches:
    #     if not match.team_one.identifier == constants.KERLA_BLASTERS_TEAM_IDENTIFIER:
    #         if not match.team_two.identifier == constants.KERLA_BLASTERS_TEAM_IDENTIFIER:
    #             filtered_matches.append(match)

    data = FootBallMatchListSerializer(matches, many=True).data
    return data


def get_kerala_blasters_matches_to_be_displayed_on_home_page():
    # from django.db.models import Q
    matches = list()
    # kerala_blasters = get_kerala_blasters_team()

    # if kerala_blasters:
    matches = FootBallMatchDetails.objects.filter(is_active=True, should_show_on_home_page=True, is_kerala_blasters_involved=True).order_by('display_priority_scale')

    data = FootBallMatchListSerializer(matches, many=True).data
    return data


def get_kerala_blasters_team():
    try:
        return SportsTeam.objects.get(identifier=constants.KERLA_BLASTERS_TEAM_IDENTIFIER)
    except SportsTeam.DoesNotExist:
        print('Failed to find kerala blasters team')
    return None

def get_recent_matches():
    return

def upcoming_matches():
    return