import traceback
from django.views.decorators.csrf import csrf_exempt
from api.decorators import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from api.source.versions.v1.services.common.football_match_services import *
from api.source.versions.v1.services.common.guest_news_service import *
from api.source.versions.v1.services.common.match_series_service import get_match_series_service
from api.source.versions.v1.services.common.news_services import *
from api.source.versions.v1.services.common.team_services import get_teams_service

log = logging.getLogger(constants.LOGGER_NAME)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def create_football_match(request, params, user_agent):
    try:

        operation = create_football_match_service(request, params, user_agent)
        if operation.status is False:
            message = messages.CREATE_FOOTBALL_MATCH_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.CREATE_FOOTBALL_MATCH_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.CREATE_FOOTBALL_MATCH_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)



@csrf_exempt
@api_view(['POST'])
@extract_request()
def update_football_match(request, params, user_agent):
    try:

        operation = update_football_match_service(request, params, user_agent)
        if operation.status is False:
            message = messages.UPDATE_FOOTBALL_MATCH_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.UPDATE_FOOTBALL_MATCH_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.UPDATE_FOOTBALL_MATCH_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def delete_football_match(request, params, user_agent):
    try:

        operation = delete_football_match_service(request, params, user_agent)
        if operation.status is False:
            message = messages.DELETE_FOOTBALL_MATCH_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.DELETE_FOOTBALL_MATCH_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.DELETE_FOOTBALL_MATCH_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)

# FOOTBALL MATCH COMMENTARY

@csrf_exempt
@api_view(['POST'])
@extract_request()
def add_football_match_commentary(request, params, user_agent):
    try:

        operation = add_football_match_commentary_service(request, params, user_agent)
        if operation.status is False:
            message = messages.ADD_FOOTBALL_MATCH_COMMENTARY_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.ADD_FOOTBALL_MATCH_COMMENTARY_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.ADD_FOOTBALL_MATCH_COMMENTARY_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)



@csrf_exempt
@api_view(['POST'])
@extract_request()
def update_football_match_commentary(request, params, user_agent):
    try:

        operation = update_football_match_commentary_service(request, params, user_agent)
        if operation.status is False:
            message = messages.UPDATE_FOOTBALL_MATCH_COMMENTARY_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.UPDATE_FOOTBALL_MATCH_COMMENTARY_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.UPDATE_FOOTBALL_MATCH_COMMENTARY_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def delete_football_match_commentary(request, params, user_agent):
    try:

        operation = delete_football_match_commentary_service(request, params, user_agent)
        if operation.status is False:
            message = messages.DELETE_FOOTBALL_MATCH_COMMENTARY_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.DELETE_FOOTBALL_MATCH_COMMENTARY_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.DELETE_FOOTBALL_MATCH_COMMENTARY_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


# FOOTBALL PLAYERS
@csrf_exempt
@api_view(['POST'])
@extract_request()
def add_football_match_player(request, params, user_agent):
    try:

        operation = add_football_match_player_service(request, params, user_agent)
        if operation.status is False:
            message = messages.ADD_MATCH_PLAYER_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.ADD_MATCH_PLAYER_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.ADD_MATCH_PLAYER_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def update_football_match_player(request, params, user_agent):
    try:

        operation = update_football_match_player_service(request, params, user_agent)
        if operation.status is False:
            message = messages.UPDATE_MATCH_PLAYER_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.UPDATE_MATCH_PLAYER_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.UPDATE_MATCH_PLAYER_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def delete_football_match_player(request, params, user_agent):
    try:

        operation = delete_football_match_player_service(request, params, user_agent)
        if operation.status is False:
            message = messages.DELETE_MATCH_PLAYER_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.DELETE_MATCH_PLAYER_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.DELETE_MATCH_PLAYER_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def add_news(request, params, user_agent):
    try:

        operation = add_news_service(request, params, user_agent)
        if operation.status is False:
            message = messages.ADD_NEWS_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.ADD_NEWS_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.ADD_NEWS_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def update_news(request, params, user_agent):
    try:

        operation = update_news_service(request, params, user_agent)
        if operation.status is False:
            message = messages.UPDATE_NEWS_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.UPDATE_NEWS_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.UPDATE_NEWS_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def delete_news(request, params, user_agent):
    try:

        operation = delete_news_service(request, params, user_agent)
        if operation.status is False:
            message = messages.DELETE_NEWS_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.DELETE_NEWS_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.DELETE_NEWS_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def get_news_details(request, params, user_agent):
    try:

        operation = get_news_details_service(request, params, user_agent)
        if operation.status is False:
            message = messages.NEWS_DETAILS_FETCH_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.NEWS_DETAILS_FETCH_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.NEWS_DETAILS_FETCH_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['GET'])
@extract_request()
def get_trending_news(request, params, user_agent):
    try:

        operation = get_trending_news_service(request, params, user_agent)
        if operation.status is False:
            message = messages.TRENDING_NEWS_FETCH_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.TRENDING_NEWS_FETCH_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.TRENDING_NEWS_FETCH_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def get_all_news(request, params, user_agent):
    try:

        operation = list_news_service(request, params, user_agent)
        if operation.status is False:
            message = messages.LIST_NEWS_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.LIST_NEWS_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.LIST_NEWS_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def add_guest_news(request, params, user_agent):
    try:

        operation = add_guest_news_service(request, params, user_agent)
        if operation.status is False:
            message = messages.ADD_GUEST_NEWS_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.ADD_GUEST_NEWS_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.ADD_GUEST_NEWS_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)



@csrf_exempt
@api_view(['POST'])
@extract_request()
def update_guest_news(request, params, user_agent):
    try:

        operation = update_guest_news_service(request, params, user_agent)
        if operation.status is False:
            message = messages.UPDATE_GUEST_NEWS_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.UPDATE_GUEST_NEWS_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.UPDATE_GUEST_NEWS_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def delete_guest_news(request, params, user_agent):
    try:

        operation = delete_guest_news_service(request, params, user_agent)
        if operation.status is False:
            message = messages.DELETE_GUEST_NEWS_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.DELETE_GUEST_NEWS_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.DELETE_GUEST_NEWS_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def list_guest_news(request, params, user_agent):
    try:

        operation = list_guest_news_service(request, params, user_agent)
        if operation.status is False:
            message = messages.LIST_GUEST_NEWS_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.LIST_GUEST_NEWS_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.LIST_GUEST_NEWS_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def guest_news_details(request, params, user_agent):
    try:

        operation = get_guest_news_details_service(request, params, user_agent)
        if operation.status is False:
            message = messages.GUEST_NEWS_DETAILS_FETCH_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.GUEST_NEWS_DETAILS_FETCH_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.GUEST_NEWS_DETAILS_FETCH_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def get_teams_list(request, params, user_agent):
    try:

        operation = get_teams_service(request, params, user_agent)
        if operation.status is False:
            message = messages.TEAMS_LIST_FETCH_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.TEAMS_LIST_FETCH_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.TEAMS_LIST_FETCH_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def get_match_series_list(request, params, user_agent):
    try:

        operation = get_match_series_service(request, params, user_agent)
        if operation.status is False:
            message = messages.MATCH_SERIES_FETCH_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.MATCH_SERIES_FETCH_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.MATCH_SERIES_FETCH_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)

