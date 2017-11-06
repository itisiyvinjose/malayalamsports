#
# import collections
# from api.localisation.constants import *
# import logging
# from django.contrib.sessions.backends.db import SessionStore
# from datetime import datetime
# import pytz
# from api.localisation.messages import *
# import time
#
# log = logging.getLogger(LOGGER_NAME)
# result = collections.namedtuple('Result', ['result', 'message'])
# session_timeout = None
# session_dict_key = 'user'
#
#
# class SessionManager(object):
#
#     def __init__(self, user=None, session_key=None):
#         self.user = user
#         self.get_session(session_key)
#
#     def user_dict(self):
#         created_at = int(time.time())
#         user_dic = {
#             "id": self.user.id,
#             "email": self.user.email,
#             "role": 'ADMIN', # TODO: remove hardcoding
#             "created_at": created_at,
#             "modified_at": created_at
#         }
#
#         return user_dic
#
#     def create_session(self):
#         self.session = SessionStore()
#         self.session[session_dict_key] = self.user_dict()
#         self.session.save()
#         self.__save_user_session()
#         return self.session.session_key
#
#     def __save_user_session(self):
#         user_session = UserSession()
#         user_session.user = self.user
#         user_session.session_id = self.session.session_key
#         user_session.save()
#
#     def get_session(self, session_key=None):
#         session_key = session_key
#         self.session = SessionStore(session_key=session_key)
#         if self.session.exists(session_key=session_key):
#             self.session.save()
#
#     def user(self):
#         return  self.user
#
#     def valid(self):
#         try:
#             if self.session and session_dict_key in self.session:
#                 data = self.session[session_dict_key]
#                 keys = ['id', 'email','created_at']
#
#                 if set(keys).issubset(data):
#                     user_id = data['id']
#
#                     try:
#
#                         self.user = User.objects.get(pk=user_id, is_active=True, is_blocked=False)
#
#                         if self.session.session_key not in self.user.sessions.all().values_list('session_id', flat=True):
#                             self.session.flush()
#                             return result(result=False, message=MESSAGE_INVALID_SESSION)
#
#                         if session_timeout:
#                             modified_date_time = datetime.utcfromtimestamp(int(data['modified_at'])).replace(tzinfo=pytz.utc)
#                             current_date_time = datetime.utcnow().replace(tzinfo=pytz.utc)
#                             delta = modified_date_time - current_date_time
#
#                             if int(delta) <= session_timeout:
#                                 self.update_session_expiry()
#                                 return result(result=True, message=None)
#
#                             else:
#                                 return result(result=False, message=MESSAGE_SESSION_TIMED_OUT)
#
#                         else:
#                             self.update_session_expiry()
#                             return result(result=True, message=None)
#                     except User.DoesNotExist:
#                         return result(result=False, message=MESSAGE_INVALID_SESSION)
#                 else:
#                     return result(result=False, message=MESSAGE_INVALID_SESSION)
#             else:
#                 return result(result=False, message=MESSAGE_INVALID_SESSION)
#         except Exception as e:
#             log.exception(msg=e)
#             message = str(e)
#             return result(result=False, message=message)
#
#     def update_session_expiry(self):
#         data = self.session[session_dict_key]
#         data['modified_at'] = int(time.time())
#         self.session[session_dict_key] = data
#         self.session.save()