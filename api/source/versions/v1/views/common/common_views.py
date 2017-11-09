import traceback
from django.views.decorators.csrf import csrf_exempt
from api.decorators import *
from api.helpers import utils
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from api.source.versions.v1.services.common.home_page_services import *
from api.source.versions.v1.services.common.news_services import *

log = logging.getLogger(constants.LOGGER_NAME)


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
@api_view(['GET'])
@extract_request()
def get_home_page_contents(request, params, user_agent):
    try:

        operation = get_home_page_contents_service(request, params, user_agent)
        if operation.status is False:
            message = messages.HOME_PAGE_FETCH_FAILURE
            response_message = utils.error_dict(message=message, detail=operation.message, error_type=operation.type)
            return error_message(response_message, status=status.HTTP_400_BAD_REQUEST, request=request)

        else:
            message = messages.HOME_PAGE_FETCH_SUCCESS
            return success_response(data=operation.data, message=message, status=status.HTTP_200_OK, request=request)

    except Exception as e:

        _traceback = traceback.format_exc()
        utils.log_request_exception(request=request, params=params, exception=e, traceback=_traceback)
        message = messages.HOME_PAGE_FETCH_FAILURE
        error_report = utils.exception_error_dict(message=message, detail=str(e))
        return error_message(error_report, status=status.HTTP_400_BAD_REQUEST, request=request)


@csrf_exempt
@api_view(['POST'])
@extract_request()
def get_news_details(request, params, user_agent):
    try:

        operation = get_news_detail_service(request, params, user_agent)
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