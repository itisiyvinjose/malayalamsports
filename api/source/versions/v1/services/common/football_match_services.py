from api.helpers import utils
from api.localisation import constants
from api.models import FootBallMatchDetails
from api.source.versions.v1.serializers.football_commentary_serializers import *
from api.source.versions.v1.serializers.football_match_serializers import *
from api.source.versions.v1.serializers.match_player_serializers import *
from api.source.versions.v1.services.base_service import *


def create_football_match_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """
    serializer = FootBallMatchSerializer(data=params, context={'request': request})
    if not serializer.is_valid():
        return result(status=False, message=serializer.errors, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)

    serializer.save()
    return result(status=True, message=None, data=serializer.data, type=None)


def update_football_match_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """

    expected_params = [
        {'name': 'match_id', 'required': True, 'type': int, 'model': FootBallMatchDetails, },
    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        football_match = FootBallMatchDetails.objects.get(id=params['match_id'])
        serializer = FootBallMatchUpdateSerializer(football_match, data=params)

        if not serializer.is_valid():
            return result(status=False, message=serializer.errors, data=None,
                          type=constants.ERROR_RESPONSE_KEY_VALIDATION)

        serializer.save()
        return result(status=True, message=None, data=serializer.data, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def get_football_match_details_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """

    expected_params = [
        {'name': 'match_id', 'required': True, 'type': int, 'model': FootBallMatchDetails, },
    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        football_match = FootBallMatchDetails.objects.get(id=params['match_id'])
        data = FootBallMatchDetailsSerializer(football_match).data
        return result(status=True, message=None, data=data, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


# def update_football_match_summary_service(request, params, user_agent):
#     """
#     create football match
#     :param request: request
#     :param params: request input params
#     :param user_agent: request user agent
#     :return: dict
#     """
#
#     expected_params = [
#         {'name': 'match_id', 'required': True, 'type': int, 'model': FootBallMatchDetails, },
#     ]
#     validation = utils.validate_request(expected_params=expected_params, request_params=params)
#     if validation.valid:
#         football_match = FootBallMatchDetails.objects.get(id=params['match_id'])
#         data = FootBallMatchDetailsSerializer(football_match).data
#         return result(status=True, message=None, data=data, type=None)
#
#     else:
#         message = validation.errors
#     return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)



def delete_football_match_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """

    expected_params = [
        {'name': 'match_id', 'required': True, 'type': int, 'model': FootBallMatchDetails, },
    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        football_match = FootBallMatchDetails.objects.get(id=params['match_id'])
        football_match.delete()
        return result(status=True, message=None, data=None, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def get_live_football_matches_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """

    matches_should_be_displayed = FootBallMatchDetails.objects.filter(is_active=True,
                                                                      should_show_on_home_page=True).all()

    if matches_should_be_displayed.count() > 0:
        final_matches_list = [matches_should_be_displayed[0]]

    else:
        final_matches_list = []

    data = FootBallMatchListSerializer(final_matches_list, many=True).data
    return result(status=True, message=None, data=data, type=None)


def get_upcoming_football_matches_service(request, params, user_agent):
    """
    get upcoming football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """

    matches_should_be_displayed = FootBallMatchDetails.objects.filter(is_active=True,
                                                                      match_status=constants.MATCH_STATUS_UPCOMING).order_by(
        'match_starting_date', 'match_starting_time').all()

    if matches_should_be_displayed.count() > 0:
        final_matches_list = [matches_should_be_displayed[0]]

    else:
        final_matches_list = []

    data = FootBallMatchListSerializer(final_matches_list, many=True).data
    return result(status=True, message=None, data=data, type=None)


def get_football_match_live_score_commentaries_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """
    expected_params = [
        {'name': 'match_id', 'required': True, 'type': int, 'model': FootBallMatchDetails, },
    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        football_match = FootBallMatchDetails.objects.get(id=params['match_id'])
        data = FootBallMatchLiveScoreCommentaryDetailsSerializer(football_match).data
        return result(status=True, message=None, data=data, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def get_football_match_live_score_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """
    expected_params = [
        {'name': 'match_id', 'required': True, 'type': int, 'model': FootBallMatchDetails, },
    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        football_match = FootBallMatchDetails.objects.get(id=params['match_id'])
        data = FootBallMatchLiveScoreSerializer(football_match).data
        return result(status=True, message=None, data=data, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def add_football_match_commentary_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """
    serializer = FootballMatchCommentarySerializer(data=params, context={'request': request})

    if not serializer.is_valid():
        return result(status=False, message=serializer.errors, data=None,
                      type=constants.ERROR_RESPONSE_KEY_VALIDATION)

    serializer.save()
    return result(status=True, message=None, data=serializer.data, type=None)


def update_football_match_commentary_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """
    expected_params = [
        {'name': 'commentary_id', 'required': True, 'type': int, 'model': FootballMatchCommentary, },
    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        match_commentary = FootballMatchCommentary.objects.get(id=params['commentary_id'])
        serializer = FootballMatchCommentaryUpdateSerializer(match_commentary, data=params)

        if not serializer.is_valid():
            return result(status=False, message=serializer.errors, data=None,
                          type=constants.ERROR_RESPONSE_KEY_VALIDATION)

        serializer.save()
        return result(status=True, message=None, data=serializer.data, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def delete_football_match_commentary_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """
    expected_params = [
        {'name': 'commentary_id', 'required': True, 'type': int, 'model': FootballMatchCommentary, },
    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        match_commentary = FootballMatchCommentary.objects.get(id=params['commentary_id'])
        match_commentary.delete()
        return result(status=True, message=None, data=None, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def list_football_match_commentary_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """
    expected_params = [
        {'name': 'match_id', 'required': True, 'type': int, 'model': FootBallMatchDetails, },
        {'name': 'offset', 'required': True, 'type': int, },
        {'name': 'limit', 'required': True, 'type': int, },

    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        match_id = params['match_id']
        offset = params['offset']
        limit = params['limit']

        commentaries = FootballMatchCommentary.objects.filter(is_active=True, football_match_id=match_id).order_by(
            '-created_at')[offset:limit]
        data = FootballMatchCommentaryDetailsSerializer(commentaries, many=True).data
        total_count = FootballMatchCommentary.objects.filter(is_active=True, football_match_id=match_id).count()
        response = {
            "content": data,
            "total_count": total_count
        }
        return result(status=True, message=None, data=response, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def add_football_match_player_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """
    serializer = FootballMatchPlayerSerializer(data=params, context={'request': request})

    if not serializer.is_valid():
        return result(status=False, message=serializer.errors, data=None,
                      type=constants.ERROR_RESPONSE_KEY_VALIDATION)

    serializer.save()
    return result(status=True, message=None, data=serializer.data, type=None)


def update_football_match_player_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """
    expected_params = [
        {'name': 'player_id', 'required': True, 'type': int, 'model': MatchPlayer, },
    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        match_player = MatchPlayer.objects.get(id=params['player_id'])
        serializer = FootballMatchPlayerUpdateSerializer(match_player, data=params)

        if not serializer.is_valid():
            return result(status=False, message=serializer.errors, data=None,
                          type=constants.ERROR_RESPONSE_KEY_VALIDATION)

        serializer.save()
        return result(status=True, message=None, data=serializer.data, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def delete_football_match_player_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """
    expected_params = [
        {'name': 'player_id', 'required': True, 'type': int, 'model': MatchPlayer, },
    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        match_player = MatchPlayer.objects.get(id=params['player_id'])
        match_player.delete()
        return result(status=True, message=None, data=None, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)


def list_football_match_player_service(request, params, user_agent):
    """
    create football match
    :param request: request
    :param params: request input params
    :param user_agent: request user agent
    :return: dict
    """
    expected_params = [
        {'name': 'match_id', 'required': True, 'type': int, 'model': FootBallMatchDetails, },

    ]
    validation = utils.validate_request(expected_params=expected_params, request_params=params)
    if validation.valid:
        match_id = params['match_id']

        players = MatchPlayer.objects.filter(is_active=True, match_id=match_id)
        data = FootballMatchPlayerDetailsSerializer(players, many=True).data
        return result(status=True, message=None, data=data, type=None)

    else:
        message = validation.errors
    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)



def upload_match_line_up_image_service(request, params, user_agent):

    if 'match_id' in params:
        match_id = int(params['match_id'])
        try:
            match = FootBallMatchDetails.objects.get(id=match_id)
            if 'image' in request.FILES and request.FILES['image']:
                image = request.FILES['image']
                match.lineup_image = image
                match.save()
                data = FootBallMatchListSerializer(match).data
                return result(status=True, message=None, data=data, type=None)
            else:
                message = '\'image\' field is required'

        except FootBallMatchDetails.DoesNotExist:
            message = 'FootBallMatchDetails with id ' + str(match_id) + ' does not exist'
    else:
        message = {
            "match_id": [
                "This field is required"
            ]
        }

    return result(status=False, message=message, data=None, type=constants.ERROR_RESPONSE_KEY_VALIDATION)

def get_upcoming_matches_service(request, params, user_agent):

    upcoming_matches = list()

    if FootBallMatchDetails.objects.filter(should_show_on_home_page=True).exists():

        reference_match = FootBallMatchDetails.objects.get(should_show_on_home_page=True)
        reference_date  = reference_match.match_starting_date

        upcoming_matches = FootBallMatchDetails.objects.filter(is_active=True, match_starting_date__gt=reference_date).all().order_by('match_starting_date')

    data = FootBallMatchListSerializer(upcoming_matches, many=True).data
    return result(status=True, message=None, data=data, type=None)



def get_previous_matches_service(request, params, user_agent):

    upcoming_matches = list()

    if FootBallMatchDetails.objects.filter(should_show_on_home_page=True).exists():

        reference_match = FootBallMatchDetails.objects.get(should_show_on_home_page=True)
        reference_date  = reference_match.match_starting_date

        upcoming_matches = FootBallMatchDetails.objects.filter(is_active=True, match_starting_date__lt=reference_date).all().order_by('-match_starting_date')

    data = FootBallMatchListSerializer(upcoming_matches, many=True).data
    return result(status=True, message=None, data=data, type=None)