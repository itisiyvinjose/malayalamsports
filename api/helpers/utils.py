import collections
import json
import logging
from django.conf import settings
from pkg_resources._vendor.appdirs import unicode

from api.localisation import constants

result = collections.namedtuple('Result', ['valid', 'errors'])


def convert_to_ist_time(date_time):
    # TODO: implement
    return None


def development_mode():
    return settings.DEBUG


def validate_request(params, data, user):
    class Context:
        missing_fields = None
        type_errors = []
        errors = dict()
        type_mapping = {
            int: 'Integer',
            str: 'String',
            list: 'Array',
            dict: 'Dictionary',
            float: 'Float',
            bool: 'Boolean'
        }

    def add_field_error(field, error):
        Context.errors[field] = error

    def validate_field(field):
        name = field['name'] if 'name' in field else None
        required = field['required'] if 'required' in field else None
        type = field['type'] if 'type' in field else None
        model = field['model'] if 'model' in field else None

        if name in data and field['type'] == str and isinstance(data[name], unicode):
            data[name] = data[name].encode('ascii', 'replace')

        field_errors = []

        if name not in data:

            if not required:
                return

            field_errors.append('This field is required.')
            add_field_error(name, field_errors)
            return

        elif type is not bool and required and not data[name]:

            if data[name] != 0:
                field_errors.append('This field value is required.')
                add_field_error(name, field_errors)
                return

        elif not isinstance(data[name], type):

            if isinstance(data[name], unicode):
                variable_type = str(data[name].encode('ascii', 'replace').__class__.__name__)

            else:
                variable_type = str(Context.type_mapping[data[name].__class__])

            field_errors.append('Expected type ' + Context.type_mapping[type] + ' but got type ' + variable_type)
            add_field_error(name, field_errors)

        elif model and type != list:
            try:

                model.objects.get(id=data[name], is_active=True)

            except model.DoesNotExist:
                model_name = model.__name__
                field_errors.append(model_name + ' with id ' + str(data[name]) + ' does not exists')
                add_field_error(name, field_errors)

    for field in params:
        validate_field(field)

    if bool(Context.errors):
        return result(valid=False, errors=Context.errors)
    else:
        return result(valid=True, errors=None)


def validation_error_dict(message, detail=None):
    error_dict = dict()
    error_dict[constants.ERROR_DICT_KEY_TYPE] = constants.ERROR_RESPONSE_KEY_VALIDATION
    error_dict[constants.ERROR_DICT_KEY_DISPLAY_MESSAGE] = message
    error_dict[constants.ERROR_DICT_KEY_DETAIL] = detail
    return error_dict


def exception_error_dict(message, detail=None):
    error_dict = dict()
    error_dict[constants.ERROR_DICT_KEY_TYPE] = constants.ERROR_RESPONSE_KEY_EXCEPTION
    error_dict[constants.ERROR_DICT_KEY_DISPLAY_MESSAGE] = message
    error_dict[constants.ERROR_DICT_KEY_DETAIL] = detail
    return error_dict


def error_dict(message, error_type, detail=None):
    error_dict = dict()
    error_dict[constants.ERROR_DICT_KEY_TYPE] = error_type
    error_dict[constants.ERROR_DICT_KEY_DISPLAY_MESSAGE] = message
    error_dict[constants.ERROR_DICT_KEY_DETAIL] = detail
    return error_dict


def log_request_exception(request, params, exception, traceback):
    exception_message = "\nException::"
    exception_message += "Request::" + str(request.get_full_path()) + ", METHOD::" + request.method
    exception_message += ",\n params=" + json.dumps(params)
    exception_message += ",\n exception=" + str(exception.message)
    exception_message += ",\n traceback=" + str(traceback)
    log = logging.getLogger(constants.LOGGER_NAME)
    log.exception(exception_message)
