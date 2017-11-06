import collections
from rest_framework import status
# from api.helpers.session import SessionManager
from api.localisation import constants, messages
# from api.permissions.permission_manager import PermissionManager

result_tuple = collections.namedtuple('Result', ['valid', 'message', 'http_status'])


class RequestValidator(object):

    def __init__(self, request, func_name,):
        self.request = request
        self.user = None
        self.session = None
        self.func_name = func_name
        self.errors = None
        self._http_status = None
        self.is_validate_invoked = False

    @property
    def errors(self):
        if self.is_validate_invoked:
            return self._errors
        else:
            raise Exception({'Exception': '\'self.validate()\' must be called before accessing \'result\' property'})

    @errors.setter
    def errors(self, value):
        self._errors = value

    @property
    def http_status(self):
        if self.is_validate_invoked:
            return self._http_status
        else:
            raise Exception(
                {'Exception': '\'self.validate()\' must be called before accessing  \'http_status\' property'})

    @http_status.setter
    def http_status(self, value):
        self._http_status = value

    def current_user(self):
        if self.is_validate_invoked:
            return self.user
        else:
            raise Exception(
                {'Exception': '\'self.validate()\' must be called before accessing  \'user\' property'})

    def current_session(self):
        if self.is_validate_invoked:
            return self.session.session
        else:
            raise Exception(
                {'Exception': '\'self.validate()\' must be called before accessing  \'session\' property'})

    # def __is_valid_session(self):
    #     if self.request.META.get('HTTP_SESSION_KEY'):
    #         self.session = SessionManager(session_key=self.request.META.get('HTTP_SESSION_KEY'))
    #         session_status = self.session.valid()
    #         if session_status.result:
    #             self.user = self.session.user
    #         else:
    #             self.errors = {
    #                             constants.ERROR_RESPONSE_KEY_SESSION:
    #                             [session_status.message]
    #                           }
    #             self.http_status = status.HTTP_401_UNAUTHORIZED
    #             return False
    #     else:
    #         self.errors = {
    #                         constants.ERROR_RESPONSE_KEY_SESSION:
    #                         [messages.MESSAGE_SESSION_KEY_ABSENT]
    #                       }
    #         self.http_status = status.HTTP_400_BAD_REQUEST
    #         return False
    #     return True

    def __authorized(self):
        # TODO: implement user agent based authorization
        return True
        # permission_manager = PermissionManager(user=self.user, func_name=self.func_name)
        # if permission_manager.access_granted():
        #     return True
        # else:
        #     message = 'You are not authorized to perform this action'
        #     self.errors = {
        #                     constants.ERROR_RESPONSE_KEY_AUTHORIZATION:
        #                     [message]
        #                   }
        #     self.http_status = status.HTTP_401_UNAUTHORIZED
        #     return False

    def __validate_request(self):
        if not self.request:
            message = 'received request with non-JSON input, Rejected.'
            self.errors = {
                            constants.ERROR_RESPONSE_KEY_REQUEST:
                            [message]
                          }
            self.http_status = status.HTTP_400_BAD_REQUEST
            return False
        return True

    def result(self, status=True):
        if self.is_validate_invoked:
            return result_tuple(valid=status, message=self.errors, http_status=self.http_status)
        else:
            raise Exception({'Exception': 'validate must be called before accessing result'})

    def valid(self):
        """
        validate request'
        :return: Boolean
        """
        self.is_validate_invoked = True

        if not self.__validate_request():
            return False

        # if not self.__is_valid_session():
        #     return False

        if not self.__authorized():
            return False

        return True