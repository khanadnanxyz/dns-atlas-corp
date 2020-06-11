from flask import jsonify


def response_builder(message, data, status_code):
    resp = {
        'status_code': status_code,
        'message': message,
        'data': data,
    }
    return jsonify(resp)
