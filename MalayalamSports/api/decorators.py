__author__ = 'Iyvin'

from functools import wraps
from api.localisation import constants, messages
import logging
from rest_framework import status
from django.http import JsonResponse
from api.helpers.request_validator import RequestValidator

log = logging.getLogger(constants.LOGGER_NAME)

OPEN_METHODS = []


def check_input():
    def wrapper(func):
        def inner_decorator(request, *args, **kwargs):
            req = json_request(request)
            if req is not None:
                if func.__name__ not in OPEN_METHODS:
                    validator = RequestValidator(request=request, func_name=func.__name__)
                    if validator.valid():
                        if func.__name__ == 'logout':
                            return func(request, req, validator.current_session(), *args, **kwargs)
                        else:
                            return func(request, req, validator.current_user(), *args, **kwargs)
                    else:
                        return error_message(validator.errors, validator.http_status)
                else:
                    return func(request, req, *args, **kwargs)
            else:
                log.info('API: Got a request with non-JSON input, Rejected.')
                message = {constants.ERROR_RESPONSE_KEY_REQUEST: messages.MESSAGE_INVALID_JSON}
                return error_message(message, status.HTTP_400_BAD_REQUEST)
        return wraps(func)(inner_decorator)
    return wrapper


def extract_request():
    def wrapper(func):
        def inner_decorator(request, *args, **kwargs):
            req = json_request(request)

            if req is not None:

                user_agent = get_user_agent(req)

                return func(request, req, user_agent, *args, **kwargs)

                # if func.__name__ not in OPEN_METHODS:
                #     return func(request, req, *args, **kwargs)
                # else:
                #     return func(request, req, *args, **kwargs)

            else:
                log.info('API: request with non-JSON input, Rejected.')
                message = {constants.ERROR_RESPONSE_KEY_REQUEST: messages.MESSAGE_INVALID_JSON}
                return error_message(message, status.HTTP_400_BAD_REQUEST)
        return wraps(func)(inner_decorator)
    return wrapper


def json_request(request):
    if request.method == 'GET':
        return request.GET

    try:
        if request.FILES:
            return request.POST
        else:
            data = request.data
            return data

    except Exception as e:
        return None

def get_user_agent(request):
    return None


def error_message(message, status, user_agent=None, request=None):
    response = dict()
    response[constants.ERROR_RESPONSE_KEY_MESSAGE] = message
    if request:
        response[constants.RESPONSE_KEY_VERSION] = request.version
    if user_agent:
        response[constants.RESPONSE_USER_AGENT] = user_agent
    return JsonResponse(response, status=status)


def success_response(data, status, user_agent=None, message=None, request=None):
    response = dict()
    response[constants.RESPONSE_DICT_RESULT_KEY] = data
    response[constants.ERROR_RESPONSE_KEY_MESSAGE] = message
    if request:
        response[constants.RESPONSE_KEY_VERSION] = request.version
    if user_agent:
        response[constants.RESPONSE_USER_AGENT] = user_agent
    return JsonResponse(response, status=status)
