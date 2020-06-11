from flask import Blueprint, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from marshmallow import ValidationError

from flask import current_app

from web.api.helper import response_builder
from web.exceptions import InvalidUsage, InvalidRequestException
from web.serializers import DataSchema
from web.services import calc_location

mod = Blueprint('v1', __name__)
data_schema = DataSchema()

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@mod.errorhandler(Exception)
def handle_invalid_usage(error):
    if isinstance(error, InvalidUsage):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    if isinstance(error, ValidationError):
        response = jsonify(error.messages)
        response.status_code = 422
        return response

    if isinstance(error, InvalidRequestException):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    response = jsonify({'message': 'Internal Server Error'})
    response.status_code = 500
    return response


@mod.route('/loc', methods=['POST'])
@limiter.limit("50 per hour")
def loc():
    json_data = request.get_json(force=True)
    if not json_data:
        raise InvalidRequestException('Request data Not valid')

    data = data_schema.load(json_data)

    x = data['x']
    y = data['y']
    z = data['z']
    vel = data['vel']
    id = current_app.config['SECTOR_ID']
    try:
        result = calc_location(id, x, y, z, vel)
        response = response_builder(message='Calculation Completed', data=result, status_code=200)
    except:
        raise InvalidUsage('This could not calculate')
    return response
