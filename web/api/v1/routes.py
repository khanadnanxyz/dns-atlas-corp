from flask import Blueprint, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from marshmallow import ValidationError

from flask import current_app

from web.api.helper import response_builder, error_response_builder
from web.exceptions import InvalidUsage, InvalidRequestException
from web.serializers import DataSchema
from web.services import calc_location

mod = Blueprint('v1', __name__)
data_schema = DataSchema()

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


# this gets all the Exceptions and response accordingly
@mod.errorhandler(Exception)
def handle_invalid_usage(error):
    if isinstance(error, InvalidUsage):
        message = error.to_dict()
        response = error_response_builder(message, error.status_code)
        return response

    if isinstance(error, ValidationError):
        message = error.messages
        response = error_response_builder(message, 422)
        return response

    if isinstance(error, InvalidRequestException):
        message = jsonify(error.to_dict())
        response = error_response_builder(message, error.status_code)
        return response

    message = 'Internal Server Error'
    response = error_response_builder(message, 500)
    return response


'''
This is the loc calculation function,
rate limiting is used 50 per hour, 
in an idea scenario, we will make it configurable.
'''


@mod.route('/loc', methods=['POST'])
@limiter.limit("50 per hour")
def loc():
    json_data = request.get_json(force=True)
    if not json_data:
        raise InvalidRequestException('Request data Not valid')

    # does the validation job
    data = data_schema.load(json_data)

    x = data['x']
    y = data['y']
    z = data['z']
    vel = data['vel']

    # gets the SECTOR_ID from env
    id = current_app.config['SECTOR_ID']
    try:
        result = calc_location(id, x, y, z, vel)
        response = response_builder(message='Calculation Completed', data=result, status_code=200)
    except:
        raise InvalidUsage('Calculated Failed')
    return response
