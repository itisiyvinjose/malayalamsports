import traceback
from django.views.decorators.csrf import csrf_exempt
# from api.authentication.auth_token_authentication import AuthTokenAuthentication
from api.decorators import *
from api.helpers import utils
# from api.permissions.view_level_access_permissions import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from api.source.versions.v1.services.common.news_services import get_trending_news_service

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