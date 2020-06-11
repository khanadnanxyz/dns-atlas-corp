from flask import Blueprint, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from marshmallow import ValidationError

from flask import current_app
from exceptions.error import InvalidUsage
from helpers.validate import DataSchema
from services.calculate import calc_distance

mod = Blueprint('v1', __name__)
data_schema = DataSchema()

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@mod.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@mod.route('/loc', methods=['POST'])
@limiter.limit("50 per hour")
def loc():
    json_data = request.get_json(force=True)
    if not json_data:
        return {'message': 'No input data provided'}, 400

    try:
        data = data_schema.load(json_data)
    except ValidationError as errors:
        return jsonify({'ok': False, 'message': 'Bad request: {}'.format(errors)}), 422

    x = data['x']
    y = data['y']
    z = data['z']
    vel = data['vel']
    id = current_app.config['SECTOR_ID']
    try:
        result = calc_distance(id, x, y, z, vel)
        response = jsonify({'loc': result}), 200
    except:
        raise InvalidUsage('This view is gone', status_code=410)
    return response
