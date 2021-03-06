import traceback
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import MultiPartParser
from api.decorators import *
from rest_framework.decorators import api_view, parser_classes
from api.source.versions.v1.services.common.football_match_services import *
from api.source.versions.v1.services.common.guest_news_service import *
from api.source.versions.v1.services.common.match_series_service import *
from api.source.versions.v1.services.common.news_services import *
from api.source.versions.v1.services.common.team_services import *

log = logging.getLogger(constants.LOGGER_NAME)


@csrf_exempt
@api_view(['POST'])
@parser_classes((MultiPartParser,))
@extract_request()
def upload_team_logo(request, params, user_agent):
    try:

        operation = upload_team_logo_service(request, params, user_agent)
        if operation.status is False:
            message = messages.TEAM_LOGO_UPDATE_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.TEAM_LOGO_UPDATE_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.TEAM_LOGO_UPDATE_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@parser_classes((MultiPartParser,))
@extract_request()
def upload_news_image(request, params, user_agent):
    try:

        operation = upload_news_image_service(request, params, user_agent)
        if operation.status is False:
            message = messages.NEWS_IMAGE_UPDATE_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.NEWS_IMAGE_UPDATE_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.NEWS_IMAGE_UPDATE_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@parser_classes((MultiPartParser,))
@extract_request()
def upload_guest_news_image(request, params, user_agent):
    try:

        operation = upload_guest_news_image_service(request, params, user_agent)
        if operation.status is False:
            message = messages.GUEST_NEWS_IMAGE_UPDATE_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.TEAM_LOGO_UPDATE_FAILURE
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.GUEST_NEWS_IMAGE_UPDATE_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@parser_classes((MultiPartParser,))
@extract_request()
def upload_match_lineup_image(request, params, user_agent):
    try:

        operation = upload_match_line_up_image_service(request, params, user_agent)
        if operation.status is False:
            message = messages.MATCH_LINEUP_IMAGE_UPDATE_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.MATCH_LINEUP_IMAGE_UPDATE_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.MATCH_LINEUP_IMAGE_UPDATE_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)



@csrf_exempt
@api_view(['POST'])
@parser_classes((MultiPartParser,))
@extract_request()
def upload_match_series_logo_image(request, params, user_agent):
    try:

        operation = upload_match_series_logo_image_service(request, params, user_agent)
        if operation.status is False:
            message = messages.MATCH_SERIES_LOGO_IMAGE_UPDATE_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.MATCH_SERIES_LOGO_IMAGE_UPDATE_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.MATCH_SERIES_LOGO_IMAGE_UPDATE_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


